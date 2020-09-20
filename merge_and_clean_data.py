#!/usr/bin/env python3
"""Exploratory analysis"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from constants import ATTRACTION_FILE_TO_CODES


def load_attractions():
    """Load attraction data as a single DataFrame"""
    return pd.concat([
        pd.read_csv('data/raw/{}'.format(f))
        .assign(
            date=lambda d: pd.to_datetime(d.date),
            datetime=lambda d: pd.to_datetime(d.datetime),
            code=ATTRACTION_FILE_TO_CODES[f]
        )
        for f in ATTRACTION_FILE_TO_CODES
    ])


def load_and_clean_data(min_date='2019-01-01', max_minutes=60*5):
    """Load attractions and join with entity"""
    attr_df = load_attractions()
    entities_df = pd.read_csv('data/raw/entities.csv')
    metadata_df = (
        pd.read_csv('data/raw/metadata.csv')
        .rename(columns={'DATE': 'date'})
        .assign(
            date=lambda d: pd.to_datetime(d.date),
        )
    )

    not_outlier = (attr_df.SACTMIN < 300) | (attr_df.SPOSTMIN < 300)

    return (
        attr_df[(attr_df.date >= min_date) & not_outlier]
        .merge(entities_df, how='left', on=['code'])
        .merge(metadata_df, how='left', on=['date'])
    )


def main():
    """Main function"""
    main_df = load_and_clean_data()

    (
        main_df[(main_df.SPOSTMIN > 0) | (main_df.SACTMIN > 0)]
        .loc[:, ['short_name', 'duration', 'SACTMIN', 'SPOSTMIN']]
        .groupby(['short_name', 'duration'])
        .describe()
        .reset_index()
        .to_csv('data/results/wait_stats.csv', index=False)
    )

    main_df.to_csv('data/clean_data.csv', index=False)


if __name__ == "__main__":
    main()
