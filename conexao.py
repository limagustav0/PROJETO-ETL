import pyodbc


def conect():
    conect = (
        "Driver={SQL Server};"
        "Server=DESKTOP-LPFPLSE\SQLEXPRESS;"
        "Database=projetoSQLPython;"
        "Trusted_Connection=yes;"
    )

    conexao = pyodbc.connect(conect)
    cursor = conexao.cursor()

    print("Conexão feita com sucesso!!")

if __name__ == "__main__":
    conect()
