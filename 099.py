import matplotlib.pyplot as plt
import seaborn as sns

dados = sns.load_dataset('titanic')

sns.countplot(dados, x='sex')

print(dados.head())
plt.show()