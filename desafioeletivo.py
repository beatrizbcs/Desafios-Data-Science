# Importar as bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import shapiro, ttest_ind, mannwhitneyu

# Dados dos grupos
grupo1 = [12, 15, 18, 22, 22, 25, 28, 30, 35, 40]
grupo2 = [15, 18, 21, 25, 25, 28, 31, 33, 38, 43]

# Cálculos: média, variância e intervalo interquartil (IQR)
media1 = np.mean(grupo1)
variancia1 = np.var(grupo1, ddof=1)
iqr1 = np.percentile(grupo1, 75) - np.percentile(grupo1, 25)

media2 = np.mean(grupo2)
variancia2 = np.var(grupo2, ddof=1)
iqr2 = np.percentile(grupo2, 75) - np.percentile(grupo2, 25)

print("Grupo 1 - Média:", media1, "Variância:", variancia1, "IQR:", iqr1)
print("Grupo 2 - Média:", media2, "Variância:", variancia2, "IQR:", iqr2)

# Teste de Shapiro-Wilk para normalidade
shapiro1 = shapiro(grupo1)
shapiro2 = shapiro(grupo2)
print("Grupo 1 - Estatística:", shapiro1.statistic, "p-valor:", shapiro1.pvalue)
print("Grupo 2 - Estatística:", shapiro2.statistic, "p-valor:", shapiro2.pvalue)

# Escolher teste estatístico (t de Student ou Mann-Whitney)
if shapiro1.pvalue > 0.05 and shapiro2.pvalue > 0.05:
    ttest = ttest_ind(grupo1, grupo2)
    print("Teste t - Estatística:", ttest.statistic, "p-valor:", ttest.pvalue)
else:
    mannwhitney = mannwhitneyu(grupo1, grupo2)
    print("Mann-Whitney - Estatística:", mannwhitney.statistic, "p-valor:", mannwhitney.pvalue)

# Criar os gráficos
plt.hist(grupo1, alpha=0.7, label="Grupo 1")
plt.hist(grupo2, alpha=0.7, label="Grupo 2")
plt.title("Histograma dos Grupos")
plt.legend()
plt.show()

sns.boxplot(data=[grupo1, grupo2], notch=True)
plt.xticks([0, 1], ["Grupo 1", "Grupo 2"])
plt.title("Boxplot Comparativo")
plt.show()