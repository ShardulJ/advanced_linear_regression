# %load q05_lasso/build.py
# Default imports
from sklearn.linear_model import Lasso
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from greyatomlib.advanced_linear_regression.q01_load_data.build import load_data

# We have already loaded the data for you

def lasso(alpha = 0.01):
    data_set, X_train, X_test, y_train, y_test = load_data('data/house_prices_multivariate.csv')
    np.random.seed(9)
    lasso_model=Lasso(alpha=alpha,normalize = True, random_state=9)
    Model = lasso_model.fit(X_train, y_train)
    y_pred_1 = lasso_model.predict(X_train)
    y_pred_2 = lasso_model.predict(X_test)
    rmse1 = float(np.sqrt(mean_squared_error(y_pred_1, y_train)))
    rmse2 = float(np.sqrt(mean_squared_error(y_pred_2, y_test)))
    return rmse1, rmse2
lasso()





