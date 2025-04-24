import pandas as pd

# morning, evening, afternoon, night
def moment_of_day(dt):
    if dt.hour < 6:
        return 'night'
    elif dt.hour < 12:
        return 'morning'
    elif dt.hour < 18:
        return 'afternoon'
    else:
        return 'evening'

def compute_daily_forecasts_per_destination(df: pd.DataFrame) -> pd.DataFrame:
    # prepare grouping keys
    df['day_date'] = df.dt.apply(lambda dt: dt.date())
    df['period_of_day'] = df.dt.apply(moment_of_day)

    daily_period_aggr_df = df.groupby(['city_id','day_date','period_of_day']).agg({
        'temp': ['mean'],
        'pop': ['mean'],
        'humidity': ['mean'],
        'wind_speed': ['mean'],
        'rain': ['sum'],
    }).unstack()
    daily_period_aggr_df.columns=daily_period_aggr_df.columns.map('.'.join)

    daily_aggr_df = df.groupby(['city_id','day_date'])[['temp', 'pop', 'humidity', 'wind_speed']].agg(['max', 'mean', 'min'])
    daily_aggr_df.columns = daily_aggr_df.columns.map('.'.join)

    return pd.merge(daily_period_aggr_df, daily_aggr_df, on=['city_id','day_date'])

def compute_weather_score(cities_weather_forecast_df: pd.DataFrame) -> pd.DataFrame:
    # Compute metrics per period of day
    daily_destinations_forecasts_df = compute_daily_forecasts_per_destination(cities_weather_forecast_df)

    # temp_score = mean of afternoon
    # pop_score = day max (worst scenario) or mean

    scoring_df = daily_destinations_forecasts_df.groupby(["city_id"]).agg(
        mean_temp=("temp.mean.afternoon", "mean"),
        min_pop=("pop.mean", "min"),
        mean_pop=("pop.mean", "mean"),
        max_pop=("pop.mean", "max")
    ).round(2)

    return scoring_df.reset_index()

# def compute_destination_score(df: pd.DataFrame) -> pd.DataFrame:
#     score = df['temp.mean.afternoon'].sum() * (100 - df['pop.mean'].mean()) / 100
#     return round(score, 2)

# def compute_ranked_destinations_on_weather_forecast(df: pd.DataFrame) -> pd.DataFrame:
#     ranked_df = df.groupby(['destination_id']).apply(compute_destination_score).rename("weather_score").reset_index()
#     return ranked_df
