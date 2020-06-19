#import pandas as pd
#dataset = pd.read_csv('train_preprocessed.csv')
#dataset['Sex'] = dataset['Sex'].map( {'female': 1, 'male': 0} )
#print("correlation score for survived and sex is: ", dataset['Survived'].corr(dataset['Sex']))

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#from sklearn.svm import SVC, LinearSVC
#from sklearn.neighbors import KNeighborsClassifier

train_df = pd.read_csv('./train.csv')
test_df = pd.read_csv('./test.csv')
combine = [train_df, test_df]
print(train_df[["Sex", "Survived"]].groupby(['Sex'], as_index=False).mean().sort_values(by='Survived', ascending=False))
#train_df = pd.read_csv('./train_preprocessed.csv')
#test_df = pd.read_csv('./test_preprocessed.csv')
#X_train = train_df.drop("Survived",axis=1)
#Y_train = train_df["Survived"]
#X_test = test_df.drop("Sex",axis=1).copy()
#print(train_df[train_df.isnull().any(axis=1)])

##SVM
#svc = SVC()
#svc.fit(X_train, Y_train)
#Y_pred = svc.predict(X_test)
#acc_svc = round(svc.score(X_train, Y_train) * 100, 2)
#print("svm accuracy is:", acc_svc)