#Michael Hamlett and Alberto Garcia
import numpy as np
import matplotlib.pyplot as plt
import datasets
from sklearn.externals import joblib

from sklearn.datasets import make_classification
from sklearn.ensemble import ExtraTreesClassifier

#Adapted from http://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html

X, y, labels, target_names, feature_names = datasets.titanic()

pipe = joblib.load('results/titanic_Imputer_Scaler_RF_pipeline.pkl')
preprocessImp = pipe.named_steps['Imputer']
preprocessSca = pipe.named_steps['Scaler']
forest = pipe.named_steps['RF']
print(pipe)

X = preprocessImp.fit_transform(X)
X = preprocessSca.fit_transform(X)

forest.fit(X, y)
importances = forest.feature_importances_
std = np.std([tree.feature_importances_ for tree in forest.estimators_],
             axis=0)
indices = np.argsort(importances)[::-1]

# Print the feature ranking
print("Feature ranking:")

for f in range(X.shape[1]):
    print("%d. feature %s (%f)" % (f + 1, feature_names[f], importances[indices[f]]))

# Plot the feature importances of the forest
plt.figure()
plt.title("Feature importances")
plt.bar(range(X.shape[1]), importances[indices],
       color="r", yerr=std[indices], align="center")
plt.xticks(range(X.shape[1]), feature_names)
plt.xlim([-1, X.shape[1]])
plt.savefig('results/titanic_feature_importances.png')
plt.show()

