#encoding=utf-8
import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing
import pandas as pd
from sklearn import datasets, linear_model

target = np.loadtxt("binary.csv", delimiter=",", skiprows=1, usecols=(0))
data = np.loadtxt("binary.csv", delimiter=",", skiprows=1, usecols=(1,2,3))

#print (set(target))
#print(target)
#print(data)

