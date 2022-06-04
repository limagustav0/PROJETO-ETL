# PROJETO-ETL

O objetivo central é extrair os dados da API pública da receita federal usando O CNPJ de empresas listadas na B3, estruturar todas as colunas de dados com Python e inserir tudo via conexão com o SQL SERVER, após isso, é feito o processo de transformação dos dados em informação utilizando o Microsoft Power BI Desktop.
Para executar o processo de extração, foi necessário criar funções de limpeza, estruturação e requisição dos dados.
Os dados serão puxados através de um laço de repetição FOR contendo uma condição que faz o loop congelar a cada 60 segundos, respeitando o tempo da API para uma nova requisição e  serem inseridos no SQL Server. 
Após o fim do loop, os dados são lidos no Power BI, é feito as relações de cardinalidade, tratamento dos tipos de dados e transformados em informação num dashboard totalmente interativo.
