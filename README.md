<p> IF697 - Introdução a Ciência de Dados </p>
<h1>Análise de Dados de Hospedagem em Recife</h1>
<h2>Vídeo Apresentação: https://drive.google.com/file/d/1Cfh9ZSbDt_jVy7ipLZknGY5Ywfh4Of6z/view</h2>

<h3>Descrição do Projeto</h3>
<br>  
<p>Este projeto visa analisar os dados de hospedagem extraídos do Booking para a cidade de Recife ao longo de um período de 12 meses. O objetivo principal é avaliar a variação dos preços dos hotéis ao longo dos meses e identificar padrões sazonais que possam indicar alta e baixa temporada. </p>

<h3>Etapas da Análise de dados</h3>
<br>
<p>
  - Extração dos dados: Utilizando Selenium foi realizada a extração dos dados da plataforma Booking. <br>
  - Carregamento dos dados: Base de dados criada a partir da extração dos dados. <br>
  - Definição dos Tipos dos dados <br>
  - Estatísticas Iniciais <br>
  - Definição dos dados ausentes <br>
  - Outliers<br>
  - Discretização <br>
  - Normalização <br>
  - Teste de Hipótese <br>
</p>

<h3> Métodos Utilizados </h3>
<br>
<p> 
  - Outiliers: <br>
  O método de Tukey foi utilizado para detectar e remover outliers. Quartis (Q1 e Q3) e a faixa interquartil (IQR) foram calculados para cada grupo de dados (mensalmente), e dados fora do intervalo aceitável foram considerados outliers e removidos. <br>
  - Normalização:
  <br>
  A normalização foi aplicada para escalar os preços de hospedagem para um intervalo entre 0 e 1, utilizando o MinMaxScaler da biblioteca scikit-learn. Isso foi necessário para garantir que os dados tivessem uma escala comparável para análises subsequentes. <br>
  - Teste de Hipótese:
  <br>
  Foi utilizado o teste de Kruskal-Wallis foi utilizado para verificar se há diferenças significativas nos preços ao longo dos meses, indicando variações sazonais. O teste de Shapiro-Wilk foi utilizado para verificar a normalidade dos dados após a transformação.
</p>

<h3> Bibliotecas Utilizadas </h3>
<br>
<p>
  - pandas <br>
  - numpy <br>
  - scipy <br>
  - sklearn <br>
  - matplotlib <br>
  - seaborn <br>
</p>

<h3> Autores </h3>
<br>
<p> Maria Clara Barretto: mcfgb@cin.ufpe.br <br>
  Geydson Renan: grml@cin.ufpe.br
</p>
