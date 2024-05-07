import pandas as pd

# Suponha que você tenha um DataFrame com uma coluna 'texto' contendo strings
# data = {'texto': ['10.2, lorem ipsum', '20.5, dolor sit amet', '30.8, consectetur adipiscing']}
# df = pd.DataFrame(data)

# # Visualize o DataFrame original
# print("DataFrame original:")
# print(df)

# # Remova os pontos e tudo o que vem depois da primeira vírgula em cada string da coluna 'texto'
# df['texto'] = df['texto'].str.replace('.', '').str.split(',').str[0]

# # Visualize o DataFrame após a modificação
# print("\nDataFrame modificado:")
# print(df)

df1 = pd.read_csv('acidentes_2020-novo.csv')
df2 = pd.read_csv('equipamentos.csv')

df2['local_instalacao'] = df2['local_instalacao'].str.replace('.', '').str.split(',').str[0].str.split(' -').str[0]

df2.to_csv('equipamentos_new.csv', index=False)




