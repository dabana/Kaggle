
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
from collections import defaultdict
from datetime import datetime
from scipy import stats
from statsmodels.formula.api import ols
import seaborn
import sklearn
from sklearn.decomposition import RandomizedPCA, PCA, SparsePCA
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from scipy import linalg as LA
from sklearn.manifold import TSNE
import time

from pubchempy import *

m = pd.read_csv('roboBohr.csv')
Id = m['pubchem_id']
t0 = time.time()
cntr = 0
f = open('compounds.csv', 'a')

for pubchemid in Id:
    try:
        cp = get_compounds(int(pubchemid), as_dataframe = True)
    except:
        print("Oups! connection broke at index = " + str(cntr))
        break
    cp.to_csv(f, header=False)
    cntr += 1
    print(cntr, end="\r")
deltat = time.time() - t0
