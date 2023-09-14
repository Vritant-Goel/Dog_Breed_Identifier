# -*- coding: utf-8 -*-

import pandas as pd
from sklearn.model_selection import train_test_split

labels = pd.read_csv('labels/labels.csv')

train, val = train_test_split(labels, train_size=0.8, random_state=0)

train.to_csv('labels/train.csv')
val.to_csv('labels/val.csv')
