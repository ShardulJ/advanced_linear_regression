# %load q01_load_data/build.py
# Default imports
import pandas as pd
from sklearn.model_selection import train_test_split
path = 'data/house_prices_multivariate.csv'

def load_data(path, test_size = 0.33, b = 9):
    df = pd.read_csv(path)
    X = df.iloc[:, :-1]
    y = df['SalePrice']
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=b, test_size=test_size)
    
    return df,X_train, X_test, y_train, y_test

df, X_train, X_test, y_train, y_test = load_data('data/house_prices_multivariate.csv')



