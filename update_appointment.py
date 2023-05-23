import sqlite3
from update_external_id import update_order_id
from external_id import insert_order_id
import csv


# Abrir arquivo com coluna com registros de work_orders + status + status do SA
with open('service_orders.csv', 'r') as f:
    dados = csv.reader(f)
    lista = list(dados)
    
conn = sqlite3.connect('nn.db')
cursor = conn.cursor()
    
""" 
    Executar loop para percorrer cada registro do arquivo
    e localizar na tabela de service orders
"""
for row in lista:
    external_id = row[0]    
    itype = row[1]
    status = row[2]
    created_at = row[3]
    closed_at = row[4]
    subscriber_id = row[5]
    address_id = row[6]
    work_order_id = row[7]
    schedule_start = row[8]
    schedule_finish = row[9]    
    status_appointment = row[10]
    
    
    cursor.execute(f"SELECT external_id FROM service_orders WHERE external_id = {external_id};")
    
    order_in_db = cursor.fetchone()
    order_in_db = list(order_in_db)
    
    
    if external_id == order_in_db[0]:
        update_order_id(external_id,itype,status,status_appointment)
        
        
    elif external_id != order_in_db[0]:
        insert_order_id(external_id,itype,status,created_at,closed_at,subscriber_id,address_id,work_order_id,schedule_start,schedule_finish,status_appointment)
        
     
        

