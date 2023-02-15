# 0 - LOAD FUNCTIONS

# standard
import numpy as np
import pandas as pd

# utilities
from sklearn.model_selection import train_test_split, GridSearchCV

# toy dataset
from sklearn.datasets import load_iris

# preprocessing
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# pipeline
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

# models
from sklearn.linear_model import LogisticRegression

# 1 - LOAD THE TOY DATASET

# load the dataset
raw_iris = load_iris()
iris = pd.DataFrame(data=np.c_[raw_iris['data'], raw_iris['target']],
                    columns=raw_iris['feature_names'] + ['target'])

# define the features - numeric and categorical
features_numeric = raw_iris['feature_names']
features_categorical = []
features_all = features_numeric + features_categorical

# split into a training and test set
X_train, X_test, y_train, y_test = train_test_split(
    iris[features_all], iris['target'], test_size=0.2, random_state=42)

# 2 - CREATE CUSTOM TRANSFORMERS

# template
class TemplateTransformer(BaseEstimator, TransformerMixin):

    """
    Template transformer class
    """

    def __init__(self):
        return None

    def fit(self, X=None, y=None):
        return self

    def transform(self, X=None):
        return self

# custom transformer to select required features
class select_features(BaseEstimator, TransformerMixin):

    """
    Transformer to select required features.

    Parameters
    ----------
    features_to_select : list[str], default=None
        The list of features to keep.
    """

    def __init__(self, features_to_select=None):

        self.features_to_select = features_to_select

    def fit(self, X, y=None):
        return self

    def transform(self, X):

        # make a copy of the df
        X_output = X.copy()

        # keep the features required
        X_output = X_output.loc[:, self.features_to_select]

        return X_output

# 3 - CREATE THE PIPELINE

    # transformer to apply on the whole dataset
all_transformer = Pipeline(steps=[
    ('select_features', select_features(features_to_select=features_all))
])

# transformer to apply on numeric features
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

# transfomer to apply on categorical features
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='error', drop='if_binary')),
])

# combine all the preprocessing steps into a single pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ('all', all_transformer, features_all),
        ('num', numeric_transformer, features_numeric),
        ('cat', categorical_transformer, features_categorical)])

# define the global pipeline - processing + model
pipe = Pipeline(steps=[('preprocessor', preprocessor),
                       ('classifier', LogisticRegression())])

# 4 - TRAIN THE BEST MODEL

# define the grid with the hyperparameters
param_grid = dict(classifier__C=[0.01, 0.1, 1],
                  classifier__penalty=['l2'],
                  classifier__max_iter=[200])

# find the best model
best_model = GridSearchCV(pipe, param_grid=param_grid,
                          cv=5, scoring='accuracy', n_jobs=-1)

# train the best model
best_model.fit(X_train, y_train)

# print the score
best_model.best_score_

# 5 - SCORE ON THE TEST SET
best_model.score(X_test, y_test)
