import os
import pandas as pd
import numpy as np
import netCDF4 as nc
import urllib


def read_data():

    lonW = -73.99  # Longitude Oeste.
    lonE = -33.86  # Longitude Leste.
    latS = -28.63  # Latitude Sul.
    latN = 5.29  # Latitude Norte.
    dgrad = .25  # Resolução do píxel.

    df = pd.read_csv('datawarehouse/focos.csv')



    print(df)


read_data()