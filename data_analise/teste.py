import os
import pandas as pd
import numpy as np
import netCDF4 as nc
import urllib


def read_data():

    def num_missing(x):
        return sum(x.isnull())

    lonW = -73.99  # Longitude Oeste.
    lonE = -33.86  # Longitude Leste.
    latS = -28.63  # Latitude Sul.
    latN = 5.29  # Latitude Norte.
    dgrad = .25  # Resolução do píxel.

    df = pd.read_csv('focos.csv')

    states = df.groupby(['estado']).ngroups

    print(states)


read_data()