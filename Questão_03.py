# Disciplina: Probabilidade e Estatística
# Aluno: JÚLIA DAPHINY LINS BRANDÃO
# Lista_6

import pandas as p #importando bibliotecas 
import seaborn as a
import matplotlib.pyplot as b

dados ={'A': [2, 3, 4, 5, 6, 7, 8, 8, 9, 10], 
		'cli': [48, 50, 56, 52, 43, 60, 62, 58, 64, 72]} #conjunto com as lista 

X = p.DataFrame (dados, columns = ['A','cli']) #define os dados e organiza
Corr = X.corr() #função da correlação para calcular o coeficiente

print(Corr) #mostra tabela com o coeficiente

a.heatmap(Corr, annot = True )
b.show() #mostra a tabela estruturada 
