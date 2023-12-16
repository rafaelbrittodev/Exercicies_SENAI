import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


gorjeta = sns.load_dataset('tips') #importação de dados

print(gorjeta.head()) #mostra o início

#Plotagem de distribuição univariada (Histogramas)

sns.histplot(gorjeta['total_bill'], kde=True, bins = 30)

#Plotagem comparada
sns.jointplot(x= 'total_bill', y= 'tip', data=gorjeta)

sns.jointplot(x= 'total_bill', y= 'tip', data=gorjeta, kind='hex')

sns.jointplot(x= 'total_bill', y= 'tip', data=gorjeta, kind= 'reg')


# Gráfico de dispersão para todas as variáveis numéricas
sns.pairplot(gorjeta)

#seleção combinada (ex: separando pelo sexo)
sns.pairplot(gorjeta, hue='sex')

#Plotagem de categorias (gráfico de barras)
sns.barplot(x='sex', y='total_bill', data=gorjeta)
sns.barplot(x='sex', y='total_bill', data=gorjeta, estimator=np.std)

sns.countplot(x='sex', data=gorjeta)


#Exibir o gráfico
plt.show()