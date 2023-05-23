
import mysql.connector
from mysql.connector import errorcode
import csv

with open('customer2.csv', 'r') as f:
    dados = csv.reader(f)
    lista = list(dados)

# ---- connect() function ----
db = mysql.connector.connect(
    option_files="wsl.ini"
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
    email = row[3]
    celular = row[4]
    telefone = row[5]
    produto = row[6]
    vencimento = row[7]    
    address_id = row[8]
    data_criacao = row[9]
   
    
         
    cursor.execute(f"""INSERT INTO customer(
        subscriber_id
        ,nome
        ,documento
        ,email
        ,celular
        ,telefone
        ,produto
        ,vencimento        
        ,address_id
        ,data_criacao) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);""",
                   (subscriber_id
                    , nome
                    , documento
                    , email
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