#Michael Hamlett and Alberto Garcia
import numpy as np
import matplotlib.pyplot as plt
import datasets
from sklearn.externals import joblib

from sklearn.datasets import make_classification

print("welcome to predict tap")

X, y, labels, target_names, feature_names = datasets.tap()

pipe = joblib.load('results/tap__KNN_pipeline.pkl')

print(X.iloc[0:1])
print(pipe.predict(X.iloc[0:1]))