import pickle
import requests
import warnings
import json

import numpy as np
import pandas as pd

from flask import Flask, request, jsonify
from sklearn.neighbors import NearestNeighbors
warnings.filterwarnings("ignore")
# app = pd.read_csv("app_encoded.csv", sep=',',
#                   index_col=0, encoding='utf8')
# # app_no_encoded = pd.read_csv("app_no_enconded_featureengineering.csv")
# app20 = app
# # # Divise app en jeu test et entrainement
# # train_set = app20.loc[~app20['Test'], :]
# test_set = app20.loc[app20['Test'], :]

# # Ensure all data is stored as floats
# train_set = train_set.astype(np.float64)
# train_set.drop(columns=["Test"], inplace=True)
# test_set = test_set.astype(np.float64)
# test_set.drop(columns=["Test"], inplace=True)

# # Target labels
# y_train = train_set['TARGET']
# y_test = test_set["TARGET"]

# # Remove test/train indicator column and target column
# x_train = train_set.drop(columns=['TARGET'])
# x_test = test_set.drop(columns=['TARGET'])

app = Flask(__name__)

with open('banking_model20.md', 'rb') as f:
    pickled_model = pickle.load(f)


@app.route('/solvabilite',methods=['POST','GET'])
def solvabilite():
    data=request.json
    data=pd.DataFrame(data, index=[0])
    data.columns = ['CREDIT_TO_ANNUITY_RATIO', 'EXT_SOURCE_1', 'EXT_SOURCE_2',
                    'EXT_SOURCE_3', 'DAYS_BIRTH', 'AMT_ANNUITY',
                    'MEDIAN(payments.AMT_PAYMENT)', 'AMT_GOODS_PRICE',
                    'DAYS_ID_PUBLISH', 'COUNT(bureau)', 'COUNT(cash_balance)',
                    'MEDIAN(cash_balance.CNT_INSTALMENT_FUTURE)', 'AMT_CREDIT',
                    'MEDIAN(prev_app.CNT_PAYMENT)',
                    'MEDIAN(bureau.DAYS_CREDIT_ENDDATE)', 'CODE_GENDER',
                    'DAYS_EMPLOYED', 'MEDIAN(bureau.AMT_CREDIT_SUM)',
                    'MEDIAN(bureau.AMT_CREDIT_MAX_OVERDUE)', 'NAME_EDUCATION_TYPE']

   
    with open('banking_model20.md', 'rb') as f:
        try:
            pickled_model = pickle.load(f)
        except:
            print('error')
    app20= pd.read_csv("app_encoded.csv", sep=',',
                      index_col=0, encoding='utf8')
    test_set = app20.loc[app20['Test'], :]
    test_set = test_set[['CREDIT_TO_ANNUITY_RATIO', 'EXT_SOURCE_1', 'EXT_SOURCE_2',
           'EXT_SOURCE_3', 'DAYS_BIRTH', 'AMT_ANNUITY',
           'MEDIAN(payments.AMT_PAYMENT)', 'AMT_GOODS_PRICE',
           'DAYS_ID_PUBLISH', 'COUNT(bureau)', 'COUNT(cash_balance)',
           'MEDIAN(cash_balance.CNT_INSTALMENT_FUTURE)', 'AMT_CREDIT',
           'MEDIAN(prev_app.CNT_PAYMENT)',
           'MEDIAN(bureau.DAYS_CREDIT_ENDDATE)', 'CODE_GENDER',
           'DAYS_EMPLOYED', 'MEDIAN(bureau.AMT_CREDIT_SUM)',
           'MEDIAN(bureau.AMT_CREDIT_MAX_OVERDUE)', 'NAME_EDUCATION_TYPE']]
    test_set
    df = test_set.iloc[:3,]
    pickled_model.predict(df)
    #solvable=pickled_model.predict(data)

    print(data)
    return "ok"
    jsonify(solvable.tolist())
    # Transformation du jeu test
    x_test_transformed = pd.DataFrame(clf_0[0].transform(x_test),
                          columns=x_test.columns,
                          index=x_test.index)

    nbrs = NearestNeighbors(n_neighbors=10, algorithm='ball_tree').fit(x_test_transformed)

    # On recupere l'indice des plus proches voisins du client  a tester
    indices = nbrs.kneighbors(x_test_transformed[0:1])[nbrs].flatten()
    app_no_encoded.iloc[indices]
    lime1 = LimeTabularExplainer(x_test_transformed,
                             feature_names=x_test.columns,
                             class_names=["Solvable", "Non Solvable"],
                             discretize_continuous=False)
                            

    exp = lime1.explain_instance(x_test_transformed.iloc[100],
                             clf_0.predict_proba,
                             num_samples=100)
    # Id client
    x_test_transformed.index["index du premier NN"]
    exp.show_in_notebook(show_table=False)

    exp.as_pyplot_figure()
    plt.tight_layout()
if __name__ == '__main__':
    app.run(debug=True, port=5002)
    #print(model)
