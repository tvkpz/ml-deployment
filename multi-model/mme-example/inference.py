
import argparse
import os
import glob

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.externals import joblib

# inference functions ---------------
def model_fn(model_dir):
    print('loading model.joblib from: {}'.format(model_dir))
    _loaded_model = joblib.load(os.path.join(model_dir, 'model.joblib'))
    return _loaded_model


if __name__ =='__main__':

    print('extracting arguments')
    parser = argparse.ArgumentParser()

    # hyperparameters sent by the client are passed as command-line arguments to the script.
    # to simplify the demo we don't use all sklearn RandomForest hyperparameters
    parser.add_argument('--n-estimators', type=int, default=10)
    parser.add_argument('--min-samples-leaf', type=int, default=3)

    # Data, model, and output directories
    parser.add_argument('--model-dir', type=str, default=os.environ.get('SM_MODEL_DIR'))
    parser.add_argument('--train', type=str, default=os.environ.get('SM_CHANNEL_TRAIN'))
    parser.add_argument('--validation', type=str, default=os.environ.get('SM_CHANNEL_VALIDATION'))
    parser.add_argument('--model-name', type=str)

    args, _ = parser.parse_known_args()

    print('reading data')
    print('model_name: {}'.format(args.model_name))

    train_file = os.path.join(args.train, args.model_name + '_train.csv')    
    train_df = pd.read_csv(train_file)

    val_file = os.path.join(args.validation, args.model_name + '_val.csv')
    test_df = pd.read_csv(os.path.join(val_file))

    print('building training and testing datasets')
    X_train = train_df[train_df.columns[1:train_df.shape[1]]] 
    X_test = test_df[test_df.columns[1:test_df.shape[1]]]
    y_train = train_df[train_df.columns[0]]
    y_test = test_df[test_df.columns[0]]

    # train
    print('training model')
    model = RandomForestRegressor(
        n_estimators=args.n_estimators,
        min_samples_leaf=args.min_samples_leaf,
        n_jobs=-1)
    
    model.fit(X_train, y_train)

    # print abs error
    print('validating model')
    abs_err = np.abs(model.predict(X_test) - y_test)

    # print couple perf metrics
    for q in [10, 50, 90]:
        print('AE-at-' + str(q) + 'th-percentile: '
              + str(np.percentile(a=abs_err, q=q)))
        
    # persist model
    path = os.path.join(args.model_dir, 'model.joblib')
    joblib.dump(model, path)
    print('model persisted at ' + path)