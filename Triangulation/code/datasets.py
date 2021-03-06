"""
Author      : Yi-Chieh Wu
Class       : HMC CS 121
Date        : 2018 Sep 24
Description : ML Datasets
"""

# python modules
import sys
import inspect

# pandas module
import pandas as pd

######################################################################
# functions
######################################################################

def iris():
    """Load iris dataset"""

    # mapping of species to integers
    target_names = ["setosa", "versicolor", "virginica"]  # display names of labels
    labels = [0, 1, 2]                                    # labels as indices
    species_map = dict(zip(map(lambda name: "Iris-%s" % name, target_names),
                            labels))

    # read csv
    df = pd.read_csv("data/iris.csv")

    # process
    df["Species"] = df["Species"].map(species_map) # map labels
    df = df.drop("Id", axis=1)      # drop Id column

    # get features, labels, and feature names
    X = df.drop("Species", axis=1)
    y = df["Species"]
    feature_names = X.columns

    return X, y, labels, target_names, feature_names



def titanic():
    """Load titanic dataset"""

    target_names = ["No", "Yes"]
    labels = [0, 1]

    # read csv
    df = pd.read_csv("data/titanic.csv")

    ### ========== TODO : START ========== ###
    # part b: process
    df = df.drop(['Ticket', 'Name', 'PassengerId', 'Cabin'], axis=1)
    df = df.replace({'female' : 0, 'male' : 1})
    df = pd.get_dummies(df, columns=['Embarked'])
    df = df.dropna(subset=['Survived'])
    #print(df.describe())
    ### ========== TODO : END ========== ###

    # get features, labels, and feature_names
    X = df.drop("Survived", axis=1)
    y = df["Survived"]
    feature_names = X.columns

    return X, y, labels, target_names, feature_names

def tap():
    """Load tap dataset"""

    target_names = ["1", "2", "3", "4"]
    labels = [0, 1, 2, 3]

    # read csv
    df = pd.read_csv("data/tap.csv")

    # get features, labels, and feature_names
    X = df.drop("Quadrant", axis=1)
    y = df["Quadrant"]
    feature_names = X.columns

    return X, y, labels, target_names, feature_names


######################################################################
# globals
######################################################################

DATASETS = [name for name, obj in inspect.getmembers(sys.modules[__name__]) if inspect.isfunction(obj)]

titanic()