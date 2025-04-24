import json
import pandas as pd
from pathlib import Path

def read_df_from_jsonlines(json_path: Path) -> pd.DataFrame:
    lines = []
    with open(json_path, "r") as f:
        lines = f.read().splitlines()

    line_dicts = [json.loads(line) for line in lines]

    return pd.DataFrame(line_dicts)

def df_postgres_upsert(table, conn, keys, data_iter):
    """
        An upsert function to allow update on existing records

        Usage:
            df.to_sql("table", db_engine, if_exists="append", index=False, method=postgres_upsert)
    """
    from sqlalchemy.dialects.postgresql import insert

    data = [dict(zip(keys, row)) for row in data_iter]

    insert_statement = insert(table.table).values(data)
    upsert_statement = insert_statement.on_conflict_do_update(
        constraint=f"{table.table.name}_pkey",
        set_={c.key: c for c in insert_statement.excluded},
    )
    conn.execute(upsert_statement)
