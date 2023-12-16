import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


gorjeta = sns.load_dataset('tips') #importação de dados

print(gorjeta.head()) #mostra o início
'''
#Plotagem de distribuição univariada (Histogramas)
sns.histplot(gorjeta['total_bill'], kde=True, bins = 30)

#Plotagem comparada
sns.jointplot(x= 'total_bill', y= 'tip', data=gorjeta)

sns.jointplot(x= 'total_bill', y= 'tip', data=gorjeta, kind='hex')

sns.jointplot(x= 'total_bill', y= 'tip', data=gorjeta, kind= 'reg')
'''
'''
# Gráfico de dispersão para todas as variáveis numéricas
sns.pairplot(gorjeta)

#seleção combinada (ex: separando pelo sexo)
sns.pairplot(gorjeta, hue='sex')

#Plotagem de categorias (gráfico de barras)
sns.barplot(x='sex', y='total_bill', data=gorjeta)
sns.barplot(x='sex', y='total_bill', data=gorjeta, estimator=np.std)

sns.countplot(x='sex', data=gorjeta)

#Diagrama de Caixas
sns.boxplot(x='day', y='total_bill', data=gorjeta)

sns.boxplot(x='day', y='total_bill', data=gorjeta, hue='snoker')

#Diagrama Violino
sns.violinplot(x= 'day', y = 'total_bill', data=gorjeta)

sns.violinplot(x= 'day', y = 'total_bill', data=gorjeta, hue= 'sex', split=True)
#---
#Gráfico de Enxame
sns.swarmplot(x='day', y='total_bill', data=gorjeta)

#Coringa
sns.catplot(x='day', y='total_bill', data=gorjeta, kind='bar')
'''
#Nova importacao
voos = sns.load_dataset('flights')

print(voos.head())

#Mapa de calor
vp = voos.pivot_table(index='month', columns='year', values='passengers')
sns.heatmap(vp, cmap='magma')

#Mapa de cluster
sns.clustermap(vp, cmap='coolwarm', standard_scale=1)

#Exibir o gráfico
plt.show()

#Para os exercicios:
#sns.load_dataset('titanic')