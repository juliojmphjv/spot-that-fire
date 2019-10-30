import pandas
from io import StringIO
from services.nrt_downloader import download_viirs_nrt_today
from os import path, listdir
from functools import reduce

dataframe_path = "data/viirs.pickle"
dataframe_incra_path = "data/incra.pickle"


def builder():

    new_data = StringIO(download_viirs_nrt_today())
    try:
        if path.isfile(dataframe_path):
            new_df = pandas.read_csv(new_data)
            old_df = pandas.read_pickle(dataframe_path)
            compare_dataframes(old_df, new_df).to_pickle(dataframe_path)
        else:
            df = pandas.read_csv(new_data)
            df.to_pickle(dataframe_path)
    except:
        pass


def compare_dataframes(old_df, new_df):
    if not old_df.equals(new_df):
        return pandas.concat((old_df, new_df), ignore_index=False)

    return old_df


def builder_incra_state(state="amazonas"):

    dataframe_list = []

    for each_file in listdir(f"incra_data/{state}"):
        dataframe_list.append(
            pandas.read_csv(
                f"incra_data/{state}/{each_file}", error_bad_lines=False
            )
        )

    return pandas.concat(dataframe_list)


def builder_incra(states=["amazonas", "acre"]):

    dataframe_list = []

    dataframe_list.append(builder_incra_state(state="amazonas"))
    dataframe_list.append(builder_incra_state(state="acre"))

    dataframe = pandas.concat(dataframe_list)
    dataframe.to_pickle(dataframe_incra_path)
