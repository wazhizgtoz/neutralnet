
import mysql.connector
from mysql.connector import errorcode
import csv

with open('customer27042023.csv', 'r') as f:
    dados = csv.reader(f)
    lista = list(dados)

# ---- connect() function ----
db = mysql.connector.connect(
    option_files="my.ini"
    )

# --- Status da conexão --- 
print(__file__ + " - Setting character set:")
print(
    "MySQL connection ID for db: {0}".format(db.connection_id)
)

# ---- Open Cursor ---- 
cursor = db.cursor()

# ---- Looping ---- 
for row in lista:
    subscriber_id = row[0]
    nome = row[1]
    documento = row[2]
    celular = row[3]
    telefone = row[4]
    produto = row[5]
    vencimento = row[6]    
    address_id = row[7]
    data_criacao = row[8]
         
    cursor.execute(f"""INSERT INTO customer(
        subscriber_id
        ,nome
        ,documento
        ,celular
        ,telefone
        ,produto
        ,vencimento        
        ,address_id
        ,data_criacao) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);""",
                   (subscriber_id
                    , nome
                    , documento
                    , celular
                    , telefone
                    , produto
                    , vencimento                    
                    , address_id
                    , data_criacao))

db.commit()

cursor.close()

db.close()

# [<=99999999999]000\.000\.000-00;00\.000\.000\/0000-00