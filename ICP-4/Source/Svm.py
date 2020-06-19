import pandas as pd
from sklearn import metrics
glassdata = pd.read_csv("glass.csv")

#Data preprocessing

X = glassdata.drop('Type', axis=1)
Y = glassdata['Type']
from sklearn.model_selection import train_test_split
X_train, X_test,Y_train, Y_test = train_test_split(X, Y, test_size=0.2,random_state=20)

# Training the algorithm
from sklearn.svm import SVC
svclassifier = SVC(kernel='linear', gamma = 'auto')
svclassifier.fit(X_train, Y_train)

#Making predictions
Y_pred = svclassifier.predict(X_test)

#Evaluating the algorithm
from sklearn.metrics import classification_report, confusion_matrix
print("accuracy score:", metrics.accuracy_score(Y_test, Y_pred))
#print(confusion_matrix(Y_test,Y_pred))
print("classification_report\n", metrics.classification_report(Y_test, Y_pred))
#print(classification_report(Y_test,Y_pred))