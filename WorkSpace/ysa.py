import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


# Veri dosya üzerinden okunur.
veriler = pd.read_csv("veri.csv")

# DATAPREPROCESSING

# Okunan veri girdi(X) ve çıktı(Y) olarak ayrıştırılır.
X =veriler.iloc[:,:4].values
Y = veriler.iloc[:,4].values

labelencoder_Y = LabelEncoder()
Y = labelencoder_Y.fit_transform(Y)
Y = np_utils.to_categorical(Y)

# Verinin %80'i train, %20'si test verisi olacak şekilde ayrılır.
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 1)

# Z-Score için normalizasyon işlemi yapılır.
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

def build_model():
    # Sıralı Model: Input Layer - Hidden Layer - Output Layer...
    model = Sequential()
    model.add(Dense(units = 32, activation = 'relu', kernel_initializer = 'uniform', input_shape = (4,)))
    # İkinci Hidden Layer katmanı
    model.add(Dense(units = 32, activation = 'relu', kernel_initializer = 'uniform'))
    # Output Layer katmanı
    model.add(Dense(units = 3, activation = 'sigmoid', kernel_initializer = 'uniform'))
    model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
    return model

classifier = build_model()
# Oluşturulan model train verileri ile eğitilir. Yapay Sinir Ağı eğitilmeye başlar.
history_callback = classifier.fit(X_train,y_train,nb_epoch=200)

acc_history = history_callback.history["acc"]


loss,accuracy = classifier.evaluate(X_test,y_test)

# Rastgele bir veri seçilerek çıktı gösterilir.
tahmin = sc.transform(np.array([5.0,2.0,3.5,1.0])).reshape(1,4)
predict = classifier.predict(tahmin)
predict_class = classifier.predict_classes(tahmin)[0]