
import pandas as pd
import pyodbc
from cnpj import puxarDados
import time
from multiplosDados import qsa,atividade


conect = (
    "Driver={SQL Server};"
    "Server=DESKTOP-LPFPLSE\SQLEXPRESS;"
    "Database=projetoSQLPython;"
    "Trusted_Connection=yes;"
)

conexao = pyodbc.connect(conect)
cursor = conexao.cursor()

if conect:
    print('Conexão feita com sucesso')

csv = pd.read_csv(r'C:\Users\gusta\OneDrive\Área de Trabalho\projeto Pessoal\B3.csv',sep=';')


codigos = csv[' ']
colunaCNPJ = csv['CNPJ']

multiplos = [numero for numero in range(0,len(colunaCNPJ)) if numero % 3 == 0]

cnpjInvalido = []

for c in range(0, len(colunaCNPJ)):

    response = puxarDados(colunaCNPJ[c])
    response['codigo'] = codigos[c]

    if len(response.keys()) < 26:
        cnpjInvalido.append(colunaCNPJ[c])
        print (f'O CNPJ abaixo está inválido: {colunaCNPJ[c]}')

        if (c in multiplos):
            print('aguardanto tempo para nova requisição')
            time.sleep(60)
    else:
        print('Inserindo Dataframes no Banco de dados...')
        pessoas = qsa(response)
        pessoas['id'] = c + 1
        for index, row in pessoas.iterrows():
            cursor.execute("INSERT INTO pessoas values(?,?,?)"
                           ,row.id,row.Nome, row.Cargo)
        atividades = atividade(response)
        atividades['id'] = c + 1
        for index, row in atividades.iterrows():
            cursor.execute("INSERT INTO atividades values(?,?,?,?,?)",
                           row.id,row.Atividade_Principal, row.Texto_Principal,
                           row.Atividade_Secundária,row.Texto_Secundário)
        df = pd.DataFrame([response])
        df_principal = df.drop(columns=['atividade_principal', 'atividades_secundarias', 'qsa', 'billing', 'extra'])
        df_principal['id'] = c + 1
        for index, row in df_principal.iterrows():
            cursor.execute("INSERT INTO dadosReceita values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                           row.id,row.data_situacao, row.complemento, row.tipo, row.nome, row.telefone, row.situacao,
                           row.bairro, row.logradouro, row.numero, row.cep, row.municipio, row.uf, row.porte,
                           row.abertura, row.natureza_juridica, row.cnpj, row.ultima_atualizacao, row.status,
                           row.fantasia, row.email, row.efr, row.motivo_situacao, row.situacao_especial,
                           row.data_situacao_especial, row.capital_social, row.codigo)

        conexao.commit()

        if (c in multiplos):
            print('aguardanto tempo para nova requisição')
            print(df_principal)
            time.sleep(60)

print(f"Os CNPJ's abaixo estão inválidos: {cnpjInvalido}")












