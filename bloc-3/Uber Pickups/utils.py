import pandas as pd
from enum import Enum

class UnpackWhat(str, Enum):
    DATE = "unpack_date"
    TIME = "unpack_time"
    ALL = "unpack_all"

UNPACK_DATE = ('date', 'year', 'month', 'week', 'day', 'day_name', 'weekday')
UNPACK_TIME = ('hour', 'minute', 'second')
UNPACK_ALL = ('all')


def unpack_datetime(data: pd.DataFrame, column: str, generate: UnpackWhat | list[str], prefix: str = None, inplace: bool = False, replace: bool=False):
    def col_name(name):
        col = name

        if prefix is not None:
            col = f'{prefix}_{name}'

        if col in data.columns and not replace:
            raise Exception(f"Sorry, column {col} already existing in dataframe")

        return col

    if isinstance(generate, UnpackWhat):
        if generate == UnpackWhat.ALL:
            selected = UNPACK_DATE + UNPACK_TIME
        elif generate == UnpackWhat.DATE:
            selected = UNPACK_DATE
        elif generate == UnpackWhat.TIME:
            selected = UNPACK_TIME
    else:
        selected = generate

    if inplace:
        holder_df = data
    else:
        holder_df = data.copy()

    if 'date' in selected:
        holder_df[col_name('date')] = holder_df[column].dt.date

    if 'year' in selected:
        holder_df[col_name('year')] = holder_df[column].dt.year

    if 'month' in selected:
        holder_df[col_name('month')] = holder_df[column].dt.month

    if 'week' in selected:
        holder_df[col_name('week')] = holder_df[column].dt.isocalendar().week

    if 'day' in selected:
        holder_df[col_name('day')] = holder_df[column].dt.day

    if 'day_name' in selected:
        holder_df[col_name('day_name')] = holder_df[column].dt.day_name()

    if 'weekday' in selected:
        holder_df[col_name('weekday')] = holder_df[column].dt.dayofweek

    if 'hour' in selected:
        holder_df[col_name('hour')] = holder_df[column].dt.hour

    if 'minute' in selected:
        holder_df[col_name('minute')] = holder_df[column].dt.minute

    if 'second' in selected:
        holder_df[col_name('second')] = holder_df[column].dt.second

    return holder_df
