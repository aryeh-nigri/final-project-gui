# Compare Algorithms
import sys
import pandas
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import train_test_split


firstName = sys.argv[1]     # string
pathToData = sys.argv[2]


fileLocation = pathToData
# tirado da primeira linha do bones.csv :
# Bone,meanGL,SD-GL,Smoothness,ThirdMoment,Uniformity,Entropy,CategoriaDoOsso
# names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
names = ["Bone", "meanGL", "SD-GL", "Smoothness", "ThirdMoment", "Uniformity", "Entropy", "CategoriaDoOsso"]
dataframe = pandas.read_csv(fileLocation, names=names)
array = dataframe.values

selected = [1,2,3,4,5,6]

data = array[:,selected]
target = array[:,7]


#pca to 2 elements and prepare graph
pca = PCA(n_components=2, svd_solver='full')
pca.fit(data)
principalComponents = pca.fit_transform(data)
principalDf = pandas.DataFrame(data = principalComponents, 
								columns = ['principal component 1', 'principal component 2'])
targetDf = pandas.DataFrame(data = target, columns = ['target'])
finalDf = pandas.concat([principalDf, targetDf], axis = 1)
finalDf.plot(kind="scatter",title="Principal Component Analisys", x="principal component 1", y="principal component 2", 
                 alpha=0.6, c="target", cmap=plt.get_cmap("jet"), colorbar=True)


# prepare configuration for cross validation test harness
seed = 7
# prepare models
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))

X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=seed)

# evaluate each model in turn
results = []
names = []
scoring = 'accuracy'
for name, model in models:
	#kfold = model_selection.KFold(n_splits=10, random_state=seed)
	cv_results = model_selection.cross_val_score(model, X_train, y_train, cv=3, scoring="accuracy")
	y_train_pred = cross_val_predict(model, X_train, y_train, cv=3)
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f %f - \n" % (name, cv_results.mean(), cv_results.std())
	print(msg)
	print(confusion_matrix(y_train, y_train_pred))
# boxplot algorithm comparison
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
sys.stdout.flush()
plt.show()
