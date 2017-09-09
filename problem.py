import numpy as np
import math
import time
import random
import itertools
import pandas as pd
from IPython.display import display, Markdown
import networkx as nx
import matplotlib.pyplot as plt


df = pd.read_excel("/home/fox/PycharmProjects/garbage/dataset-HP.xls",sheetname="eil51", header=None, index_col=0)

df.columns = ['x','y','garbage']

display(df[0:10])

distances = [-1]
garbage = [-1]

for lab, row in df.iterrows():
    tempDist = [-1]
    garbage.append(row['garbage'])
    for lab2, row2 in df.iterrows():
        dist = math.sqrt(math.pow(row['x'] - row2['x'], 2) + math.pow(row['y'] - row2['y'], 2))
        tempDist.append(dist)
    distances.append(tempDist)

dff = [[0, 0, 0]]
for lab, row in df.iterrows():
    dff.append([row['x'], row['y'], row['garbage']])

