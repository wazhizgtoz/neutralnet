"""
    Autor: Washington Silva do Espírito Santo
    Programa: Inserir registros de ordens de serviço na tabela service_orders
    Data: 08/03/2023
    Versão: 01    
"""
import mysql.connector
from mysql.connector import errorcode
import csv

with open('service_orders.csv', 'r',encoding='latin-1') as f:
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

for row in lista:
    external_id = row[0]
    type = row[1]
    status = row[2]          
    created_at = row[3]
    closed_at = row[4]
    subscriber_id = row[5]
    address_id = row[6]    
    work_order_id = row[7]
    schedule_start = row[8]
    schedule_finish = row[9]        
    status_appointment = row[10]
    
    cursor.execute(f"""
                   INSERT INTO service_orders(external_id
                         ,type
                         ,status                         
                         ,created_at
                         ,closed_at
                         ,subscriber_id
                         ,address_id
                         ,work_order_id
                         ,schedule_start
                         ,schedule_finish                         
                         ,status_appointment) 
                   VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);""", 
                        (external_id
                         ,type
                         ,status                         
                         ,created_at
                         ,closed_at
                         ,subscriber_id
                         ,address_id
                         ,work_order_id
                         ,schedule_start
                         ,schedule_finish                          
                         ,status_appointment))

db.commit()

cursor.close()

db.close()


         