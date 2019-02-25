import pandas as pd

base = pd.read_csv("./bones.csv")
               
previsores = base.iloc[:, 1:7].values
classe = base.iloc[:, 7].values

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)

from sklearn.cross_validation import train_test_split
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, classe, test_size=0.25)#, random_state=0)

from sklearn.svm import SVC
classificador = SVC(kernel = 'rbf', random_state = 1, C = 2.0)
classificador.fit(previsores_treinamento, classe_treinamento)
previsoes = classificador.predict(previsores_teste)

from sklearn.metrics import confusion_matrix, accuracy_score
precisao = accuracy_score(classe_teste, previsoes)
matriz = confusion_matrix(classe_teste, previsoes)

import collections
collections.Counter(classe_teste)

print("Precisao de " + str(precisao * 100) + "%")