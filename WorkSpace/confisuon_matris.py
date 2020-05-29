import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn import metrics

"""print(__doc__)"""

veriler = pd.read_csv("../Datas/birlestirilmisVeriler.csv")

x = veriler.iloc[:,1:4].values

y = veriler.iloc[:,6:7].values


x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0)

classifier = svm.SVC(kernel='linear', C=0.02).fit(x_train, y_train)
classifier = KNeighborsClassifier(n_neighbors=3, metric="minkowski").fit(x_train,y_train)
classifier =RandomForestClassifier(n_estimators=2, criterion='entropy').fit(x_train,y_train)

np.set_printoptions(precision=2)

titles_options = [("KNN Algoritması", None),
                  ("SVM Algoritması ", 'true'),
                  ("Random Forest Algoritması" ,None
                   )
                  ]
for title, normalize in titles_options:
    disp = plot_confusion_matrix(classifier, x_test, y_test,
                                 display_labels='101111111111111111111',
                                 cmap=plt.cm.Blues,
                                 normalize=normalize)
    disp.ax_.set_title(title)

    print(title)
    print(disp.confusion_matrix)

plt.show()