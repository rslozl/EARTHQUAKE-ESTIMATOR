import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
import matplotlib.pyplot as plt


veriler = pd.read_csv("../Datas/birlestirilmisVeriler.csv")

x = veriler.iloc[:,1:4].values

y = veriler.iloc[:,6:7].values

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=2, test_size= 0.33)

"""print(x_test)"""

rdf = RandomForestClassifier(n_estimators=3, criterion='entropy')
rdf.fit(x_train,y_train)
y_pred = rdf.predict(x_test)

cm = confusion_matrix(y_test,y_pred)
print(cm,"random forest algoritmasi")
print("Random Forest Algoritması Doğruluk Oranı: {}".format(accuracy_score(y_test, y_pred)))


knn = KNeighborsClassifier(n_neighbors=3,metric="minkowski")


knn.fit(x_train, y_train)

y_pred = knn.predict(x_test)


cs = confusion_matrix(y_test,y_pred)


print(cs,"knn algoritmasi:")

print("Knn  Algoritması Doğruluk Oranı: {}".format(accuracy_score(y_test, y_pred)))


svc = SVC(kernel="linear")
svc.fit(x_train, y_train)
y_pred0 = svc.predict(x_test)

cs2 = confusion_matrix(y_test,y_pred)

print(cs2, "svm algoritması doğruluk oranı:")
print("SVM  Algoritması Doğruluk Oranı: {}".format(accuracy_score(y_test, y_pred0)))
