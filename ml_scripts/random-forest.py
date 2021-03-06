import pandas as pd

base = pd.read_csv("./bones.csv")

base.describe()

previsores = base.iloc[:, 1:7].values
classe = base.iloc[:, 7].values

"""
Faz o escalonamento dos dados, para algoritmos como KNN nao darem
maior importancia para valores mais altos, alem de acelerar o 
processo em datasets muito grandes.
"""
"""
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)
"""
# separa o dataset em treinamento e teste, de acordo com a porcentagem de teste escolhida
# random_state=1 faz a funcao escolher aleatoriamente os dados para teste
from sklearn.cross_validation import train_test_split
test_percentage = 0.20
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, classe, test_size=test_percentage, random_state=1)

# Cria a floresta de decisao
from sklearn.ensemble import RandomForestClassifier
classificador = RandomForestClassifier(n_estimators=50, criterion='entropy')#, random_state=0)
classificador.fit(previsores_treinamento, classe_treinamento)
previsoes = classificador.predict(previsores_teste)

# testa o modelo
from sklearn.metrics import confusion_matrix, accuracy_score
# porcentagem de acerto
precisao = accuracy_score(classe_teste, previsoes)
# acertos em matriz
matriz = confusion_matrix(classe_teste, previsoes)

print("Precisao de " + str(precisao * 100) + "%")