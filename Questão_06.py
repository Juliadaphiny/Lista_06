# Disciplina: Probabilidade e Estatística
# Aluno: JÚLIA DAPHINY LINS BRANSÃO
# Lista_6

import pandas as p #importando bibliotecas 

dados ={'P': [100, 102, 105, 108, 112, 120], 
		'A': [4, 5, 1, 3, 6, 2]} #conjunto com as lista

X = p.DataFrame (dados, columns = ['P','A']) #define os dado e organiza
Corr = X.corr() #função da correlação para calcular o coeficiente

print('O COEFICIENTE DE CORRELAÇÃO LINEAR É:')
print(Corr) #mostra tabela com o coeficiente
