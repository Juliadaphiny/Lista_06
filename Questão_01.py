# Disciplina: Probabilidade e Estatística
# Aluno: JÚLIA DAPHINY LINS BRANSÃO
# Lista_6

import seaborn as a
import matplotlib.pyplot as b
import pandas as p #importando bibliotecas 

dados ={'criança': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 
		'mat': [60, 58, 73, 51, 54, 75, 48, 72, 75, 83, 62, 52],
		'mus': [80, 62, 70, 83, 62, 92, 79, 88, 54, 82, 64, 69]} #conjunto com as listas 

X = p.DataFrame (dados, columns = ['criança','mat','mus']) #define os dado e organiza
Corr = X.corr() #função da correlação para calcular o coeficiente

print(Corr) #mostra tabela 

a.heatmap(Corr, annot = True )
b.show() #mostra a tabela estruturada 
