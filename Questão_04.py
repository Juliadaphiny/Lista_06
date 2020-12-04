# Disciplina: Probabilidade e Estatística
# Aluno: JÚLIA DAPHINY LINS BRANSÃO
# Lista_6

import pandas as p #importando bibliotecas 
import seaborn as a
import matplotlib.pyplot as b

dados ={'X': [12, 16, 18, 20, 28, 30, 40, 48, 50, 54], 
		'Y': [7.2, 7.4, 7.0, 6.5, 6.6, 6.7, 6.0, 5.6, 6.0, 5.5]} #conjunto com as lista 

X = p.DataFrame (dados, columns = ['X','Y']) #define os dados e organiza
Corr = X.corr() #função da correlação para calcular o coeficiente

print(Corr) #mostra tabela com o coeficiente

a.heatmap(Corr, annot = True )
b.show() #mostra a tabela estruturada 
