import sys
import pandas as pd
import sklearn as sk


# sys.argv is an array of strings
# ('python', ['./ml_scripts/classifier.py', firstName, lastName, gender, birthday, exam1, exam2, exam3, pacsFile]);
# firstName = sys.argv[1]     # string
# lastName = sys.argv[2]      # string
# gender = sys.argv[3]        # male/female
# birthday = sys.argv[4]      # date
# exam1 = sys.argv[5]         # string
# exam2 = sys.argv[6]         # string
# exam3 = sys.argv[7]         # string
# pacsFile = sys.argv[8]      # file

# print("python script called from nodejs\n")
# print(firstName + "\t" + lastName + "\n" + gender + "\n" + birthday + "\n" + exam1 + "\n" + exam2 + "\n" + exam3 + "\n" + pacsFile)

fileLocation = r"c:/Users/Arieh/Documents/5779.1/WebDevelopment/targil2/login-form/ml_scripts/bones.csv"
base = pd.read_csv(fileLocation)

base.describe()

previsores = base.iloc[:, 1:7].values
classe = base.iloc[:, 7].values

# from sklearn.preprocessing import StandardScaler
# scaler = StandardScaler()
scaler = sk.preprocessing.StandardScaler()
previsores = scaler.fit_transform(previsores)

# separa o dataset em treinamento e teste, de acordo com a porcentagem de teste escolhida
# random_state=0 faz a funcao NAO escolher aleatoriamente os dados para teste
# from sklearn.cross_validation import train_test_split
test_percentage = 0.20
# previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, classe, test_size=test_percentage, random_state=0)
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = sk.cross_validation.train_test_split(previsores, classe, test_size=test_percentage, random_state=0)

# cria a tabela gaussiana, o modelo classificador
# from sklearn.naive_bayes import GaussianNB
# classificador = GaussianNB()
classificador = sk.naive_bayes.GaussianNB()
classificador.fit(previsores_treinamento, classe_treinamento)
previsoes = classificador.predict(previsores_teste)

# testa o modelo
# from sklearn.metrics import confusion_matrix, accuracy_score
# porcentagem de acerto
# precisao = accuracy_score(classe_teste, previsoes)
precisao = sk.metrics.accuracy_score(classe_teste, previsoes)
# acertos em matriz
# matriz = confusion_matrix(classe_teste, previsoes)
matriz = sk.metrics.confusion_matrix(classe_teste, previsoes)

print("Precisao de " + str(precisao))