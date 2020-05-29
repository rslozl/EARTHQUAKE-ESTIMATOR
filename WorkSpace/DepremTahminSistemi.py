import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn import metrics



def depremTahmincisi(input_list):
    veriler = pd.read_csv("../Datas/birlestirilmisVeriler.csv")

    x_train = veriler.iloc[:,1:4].values
    y_train= veriler.iloc[:,6:7].values




    svc = SVC(kernel="linear")
    svc.fit(x_train,y_train)
    y_pred0 = svc.predict(input_data)



    print(y_pred0, " support vector machine yontemine gore tahmin")

    rdf = RandomForestClassifier(n_estimators=1, criterion='entropy')
    rdf.fit(x_train, y_train)
    y_pred  = rdf.predict(input_data)
    print(y_pred, " random_forest yontemine gore tahmin")

    knn = KNeighborsClassifier(n_neighbors=3, metric="minkowski")

    knn.fit(x_train, y_train)

    y_pred2 = knn.predict(input_data)


    print(y_pred2, "knn algoritmasina gore tahmin")







"""
#burada modelleri bir listenin içerisine alıp parametreleri ile beraber tanımlıyoruz.
models = []
models.append(('K-NN', KNeighborsClassifier()))
models.append(('SVM', SVC()))
models.append(('RandomForestClassifier', RandomForestClassifier()))

#burada bir döngü vasıtasıyla tek tek bütün modelleri deneyerek sonuçları karşılaştırıyoruz.
for name, model in models:
    model = model.fit()
    y_pred = model.predict()
    from sklearn import metrics

    print("%s -> ACC: %%%.2f" % (name,metrics.accuracy_score(y_pred)*100))
    print("dsd")

"""








if __name__ == '__main__':

    depremDerinligi = input("Lutfen olabilecek depremin olmasi muhtemel fay hattı derinligini giriniz :")
    yeraltiSuYuksekligi = input("Lutfen yeraltisu kaynaklarinin yuksekligini giriniz:")
    radonGazi = input("radon gazi seviyesini giriniz: ")
    metanGazi=input("metan gazi seviyesini giriniz")

    input_data = [[float(depremDerinligi),float(radonGazi),float(yeraltiSuYuksekligi)]]


    depremTahmincisi(input_data)











