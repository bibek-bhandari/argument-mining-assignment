from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import pandas
import numpy as np
import joblib
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import roc_auc_score

data_X = []
data_Y = []
with open('data/traindata.txt') as fp:
    # 1. iterate over file line-by-line
    # 2. strip line of newline symbols
    # 3. split line by spaces into list (of number strings)
    # 4. convert number substrings to int values
    # 5. convert map object to list

    for line in fp:
    	if(len(line.strip().split('\t')) > 1):
    		data_X.append(line.strip().split('\t')[0])
    		data_Y.append(line.strip().split('\t')[1])



feature_extraction = TfidfVectorizer()
data_X_vector = feature_extraction.fit_transform(data_X)
joblib.dump(feature_extraction, 'feature_extraction.pkl')

parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10]}
svc = SVC()
clf = GridSearchCV(svc, parameters)

#clf = SVC(probability=True, kernel='rbf',C=10)
classifier=clf.fit(data_X_vector, data_Y)
joblib.dump(clf, 'my_dumped_classifier.pkl')


#print('ROC-AUC yields ' + str(roc_auc_score(test_Y, predictions,multi_class="ovo")))