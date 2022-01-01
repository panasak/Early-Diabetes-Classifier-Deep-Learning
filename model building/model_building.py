# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file

"""
import pandas as pd

df = pd.read_csv(r"C:\Users\tango\Documents\GitHub\Deep-learning-placeholder\title_basics.csv")

df = df.drop(['tconst','primaryTitle','originalTitle','endYear','runtimeMinutes'],axis=1)

df = df[df['startYear'] != '\\N']

df['genres']= df['genres'].apply(lambda x : x.split(','))

pd.get_dummies(df['genres'].apply(pd.Series).stack()).sum(level=0)