import sys
import os
home_directory_path = os.path.expanduser('~')
sys.path.append(home_directory_path +'/utils')
from prepare_utils import split_data

import numpy as np
import pandas as pd

from sklearn.preprocessing import MinMaxScaler

from sklearn.metrics import mean_squared_error, r2_score

from sklearn.dummy import DummyRegressor

def preprocess_zillow_data(df):
    
    stratify_col = ['county']
    target = ['property_value']
    
    df['1_2_bathrooms'] = np.where(df['bathrooms'] <= 2, 1, 0)
    df['2.5_3_bathrooms'] = np.where(df['bathrooms'].isin([2.5, 3]), 1, 0)
    df['3.5_4_bathrooms'] = np.where(df['bathrooms'] >= 3.5, 1, 0)
    
    features = ['sqft','1_2_bathrooms','2.5_3_bathrooms','3.5_4_bathrooms']
    
    train, validate, test = split_data(df[features+target+stratify_col],
                                       validate_size=.15, test_size=.15, 
                                       stratify_col=stratify_col, random_state=123)

    # drop county column
    train = train[features+target]
    validate = validate[features+target]
    test = test[features+target]
    

    
    # remove target
    X_train = train[features]
    X_validate = validate[features]
    X_test = test[features]

    # only add target
    y_train = train[target]
    y_vaildate = validate[target]
    y_test = test[target]
    
    scaler = MinMaxScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_validate_scaled = scaler.transform(X_validate)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_validate_scaled, X_test_scaled,\
            y_train, y_vaildate, y_test, scaler


def run_model(X_train, y_train, X, y, model, scaler, features):
    
    train_model = model.fit(X_train, y_train)
    
    train_rmse = mean_squared_error(y_train,
                              model.predict(X_train),
                              squared=False)
    test_rmse = mean_squared_error(y,
                              model.predict(X),
                              squared=False)
    train_r2 = model.score(X_train, y_train)
    test_r2 = model.score(X, y)
    
    if isinstance(model, DummyRegressor):
        return train_rmse, test_rmse, train_r2, test_r2
    
    display(pd.DataFrame(index=features + ['intercept'],
                         columns=['coefficients'],
                         data=np.append(model.coef_ * scaler.scale_, model.intercept_)))
    
    coeffs = np.append(model.coef_, model.intercept_)
    coeffs_unscaled = np.append(model.coef_ * scaler.scale_, model.intercept_)
    
    return train_rmse, test_rmse, train_r2, test_r2, coeffs, coeffs_unscaled 