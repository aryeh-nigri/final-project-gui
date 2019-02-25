# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 15:46:36 2018

@author: Arieh
"""

import Orange

base = Orange.data.Table('credit_data.csv')
base.domain

base_dividida = Orange.evaluation.testing.sample(base, n=0.25)
base_treinamento = base_dividida[1]
base_teste = base_dividida[0]
len(base_treinamento)
len(base_teste)

# Majority Learner, ou classificacao base, nao eh um algoritmo de aprendizado.
# Ele apenas conta cada instancia e aquele que for maioria sera a classe sempre.
# Ele eh base pq se um modelo nao passar da avaliacao do Majority Learner, entao
# nem deveria usa-lo, e sim usar o proprio Majority Learner de uma vez.
# Tambem eh conhecido por ZeroR(zero rules).
classificador = Orange.classification.MajorityLearner()
resultado = Orange.evaluation.testing.TestOnTestData(base_treinamento, base_teste, [classificador])
print(Orange.evaluation.CA(resultado))

from collections import Counter
print(Counter(str(d.get_class()) for d in base_teste))

# base line classifier