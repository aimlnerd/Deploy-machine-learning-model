import sys
import os
import shutil
import time
import traceback

from flask import Flask, request, jsonify
import pandas as pd
from sklearn.externals import joblib

app = Flask(__name__)

# inputs
training_data = 'data/titanic.csv'
include = ['Age', 'Sex', 'Embarked', 'Survived']
dependent_variable = 'Survived'

model_directory = 'model'
model_file_name = f'{model_directory}/model.pkl'
model_columns_file_name = f'{model_directory}/model_columns.pkl'

# These will be populated at training time
model_columns = None
clf = None


@app.route('/predict', methods=['POST']) # Create http://host:port/predict POST end point
def predict():
    if clf:
        try:
            json_ = request.json #capture the json from POST
            query = pd.get_dummies(pd.DataFrame(json_))
            query = query.reindex(columns=model_columns, fill_value=0)

            prediction = list(clf.predict(query))

            return jsonify({'prediction': [int(x) for x in prediction]})

        except Exception as e:

            return jsonify({'error': str(e), 'trace': traceback.format_exc()})
    else:
        print('train first')
        return 'no model here'


@app.route('/train', methods=['GET']) # Create http://host:port/train GET end point
def train():
    # using random forest as an example
    # can do the training separately and just update the pickles
    from sklearn.ensemble import RandomForestClassifier as rf

    df = pd.read_csv(training_data)
    df_ = df[include]

    categoricals = []  # going to one-hot encode categorical variables

    for col, col_type in df_.dtypes.iteritems():
        if col_type == 'O':
            categoricals.append(col)
        else:
            df_[col].fillna(0, inplace=True)  # fill NA's with 0 for ints/floats, too generic

    # get_dummies effectively creates one-hot encoded variables
    df_ohe = pd.get_dummies(df_, columns=categoricals, dummy_na=True)

    x = df_ohe[df_ohe.columns.difference([dependent_variable])]
    y = df_ohe[dependent_variable]

    # capture a list of columns that will be used for prediction
    global model_columns
    model_columns = list(x.columns)
    joblib.dump(model_columns, model_columns_file_name)

    global clf
    clf = rf()
    start = time.time()
    clf.fit(x, y)
    print('Trained in %.1f seconds' % (time.time() - start))
    print('Model training score: %s' % clf.score(x, y))

    joblib.dump(clf, model_file_name)

    return 'Success'


@app.route('/wipe', methods=['GET']) # Create http://host:port/wipe GET end point
def wipe():
    try:
        shutil.rmtree('model')
        os.makedirs(model_directory)
        return 'Model wiped'

    except Exception as e:
        print(str(e))
        return 'Could not remove and recreate the model directory'


if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
    except Exception as e:
        port = 80

    try:
        clf = joblib.load(model_file_name)
        print('model loaded')
        model_columns = joblib.load(model_columns_file_name)
        print('model columns loaded')

    except Exception as e:
        print('No model here')
        print('Train first')
        print(str(e))
        clf = None

    app.run(host='0.0.0.0', port=port, debug=False)
