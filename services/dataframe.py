import pandas
from io import StringIO
from services.nrt_downloader import download_viirs_nrt_today
from os import path


dataframe_path = "data/dataframe.pickle"


def builder():

    new_data = StringIO(download_viirs_nrt_today())

    if path.isfile(dataframe_path):
        new_df = pandas.read_csv(new_data)
        old_df = pandas.read_pickle(dataframe_path)
        compare_dataframes(old_df, new_df).to_pickle(dataframe_path)
    else:
        df = pandas.read_csv(new_data)
        df.to_pickle(dataframe_path)


def compare_dataframes(old_df, new_df):
    if not old_df.equals(new_df):
        old_df = old_df.concat(new_df, ignore_index=False)
        return old_df

    return old_df


builder()
