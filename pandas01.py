# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 08:59:09 2024

@author: ITUMELENG
"""

import pandas
file = pandas.read_csv("country_data.csv")
print(file)
print(file.info())
print(file.describe())