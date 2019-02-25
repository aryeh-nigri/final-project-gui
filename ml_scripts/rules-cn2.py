# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 15:42:04 2018

@author: Arieh
"""

import Orange

# precisa mudar o arquivo csv e escrever c# antes do nome da classe
base = Orange.data.Table('result-machine-learning-living-bone-ezor-1.csv')
base.domain

base_dividida = Orange.evaluation.testing.sample(base, n=0.20)
base_treinamento = base_dividida[1]
base_teste = base_dividida[0]
len(base_treinamento)
len(base_teste)

cn2_learner = Orange.classification.rules.CN2Learner()
classificador = cn2_learner(base_treinamento)

for regras in classificador.rule_list:
    print(regras)
    
resultado = Orange.evaluation.testing.TestOnTestData(base_treinamento, base_teste, [classificador])
print(Orange.evaluation.CA(resultado))


"""

cn2_learner = Orange.classification.rules.CN2Learner()
classificador = cn2_learner(base)
for regras in classificador.rule_list:
    print(regras)
    
# história boa, dívida alta, garantias nenhuma, renda > 35
# história ruim, dívida alta, garantias adequada, renda < 15
resultado = classificador([['boa', 'alta', 'nenhuma', 'acima_35'], ['ruim', 'alta', 'adequada', '0_15']])
for i in resultado:
    print(base.domain.class_var.values[i])
    
"""