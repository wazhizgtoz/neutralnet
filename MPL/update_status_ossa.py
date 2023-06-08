import mysql.connector
from mysql.connector import errorcode
from update_service_order import update_status
from insert_service_order import insert_new_service_order
import csv



"""" Abrir arquivo de registros de service orders + status + status do SA """
with open('service_order_ret.csv', 'r') as f:
    dados = csv.reader(f)
    lista = list(dados) 
    
""" 
    Executar loop para percorrer cada registro do arquivo
    e localizar na tabela de service orders
"""
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
    
    db = mysql.connector.connect(option_files="my.ini")
    
    cursor = db.cursor()    
    
    cursor.execute(f"SELECT external_id FROM service_orders WHERE external_id = {external_id};")

    result = cursor.fetchall()
    
    for external in result:
        
        service_order = external[0] 
        
        try:    
    
            if service_order == external_id:
                update_status(status,status_appointment,closed_at,external_id)

            elif service_order != external_id:
                insert_new_service_order(external_id,type,status,created_at,closed_at,subscriber_id,address_id,work_order_id,schedule_start,schedule_finish,status_appointment)
            
            else:
                """ Abrir arquivo de registros de service orders + status + status do SA """
                with open('service_order_inst.csv', 'r') as f:
                    dados = csv.reader(f)
                    lista = list(dados)
                    
        except mysql.connector.errors.DataError:
            print(subscriber_id,closed_at)
            print('no banco',service_order)
            print('no arquivo',external_id)
            
            
            pass
            continue