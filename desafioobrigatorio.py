# Importar as bibliotecas necessárias
import pandas as pd
import numpy as np

# **Passo 1: Criar o arquivo vendas.xlsx com os dados fornecidos**
dados = {
    "Região": ["Norte", "Norte", "Sul", "Sul", "Norte"],
    "Mês": ["Jan", "Fev", "Jan", "Fev", "Mar"],
    "Vendas": [1500, None, 2200, 1800, 2000],  # None representa valores ausentes (NA)
    "Despesas": [300, 250, None, 400, 350]    # None também usado para valores ausentes
}

# Criar o DataFrame com os dados
df = pd.DataFrame(dados)

# Salvar o DataFrame inicial como um arquivo Excel (opcional, para visualizar os dados originais)
df.to_excel("vendas_inicial.xlsx", index=False)
print("Arquivo 'vendas_inicial.xlsx' criado com os dados originais (valores ausentes intactos).")

# **Passo 2: Substituir valores ausentes**
# Substituir valores ausentes na coluna "Vendas" pela mediana
mediana_vendas = df["Vendas"].median()  # Calcula a mediana
df["Vendas"].fillna(mediana_vendas, inplace=True)  # Substitui NaN pela mediana

# Substituir valores ausentes na coluna "Despesas" pela média
media_despesas = df["Despesas"].mean()  # Calcula a média
df["Despesas"].fillna(media_despesas, inplace=True)  # Substitui NaN pela média

print("\nDados após substituição dos valores ausentes:")
print(df)

# **Passo 3: Agrupar os dados e calcular**
# Agrupar os dados por "Região" e "Mês"
agrupados = df.groupby(["Região", "Mês"]).agg(
    Soma_Vendas=("Vendas", "sum"),  # Soma total de vendas
    Media_Despesas=("Despesas", "mean")  # Média das despesas
).reset_index()

print("\nDados agrupados por Região e Mês:")
print(agrupados)

# **Passo 4: Combinar colunas horizontalmente (hstack)**
# Combinar as colunas "Vendas" e "Despesas" lado a lado
combinacao = np.hstack((df["Vendas"].values.reshape(-1, 1), df["Despesas"].values.reshape(-1, 1)))

print("\nCombinação horizontal de Vendas e Despesas:")
print(combinacao)

# **Passo 5: Gerar um sumário estatístico**
# Gerar um resumo estatístico para as colunas numéricas
resumo = {
    "Média": df.mean(numeric_only=True),
    "Mediana": df.median(numeric_only=True),
    "Desvio Padrão": df.std(numeric_only=True)
}

resumo_df = pd.DataFrame(resumo)
print("\nResumo estatístico das colunas numéricas:")
print(resumo_df)

# **Salvar o arquivo Excel atualizado**
df.to_excel("vendas.xlsx", index=False)
print("\nArquivo 'vendas.xlsx' criado com os dados tratados (valores ausentes substituídos).")