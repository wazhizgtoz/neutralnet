""" Programa que irá buscar no banco de dados todos os registros de ordem de instalação 
    e ordens de retirada (Cancelamento de produto) solicitados pelo mesmo Cliente para 
    endereços diferentes, que caracteriam solicitação de mudança de endereço. As solicitações
    deve ser no mesmo periodo de data.

    author: Washington do Espírito Santo
    Version: 1.0
"""
import mysql.connector
from mysql.connector import errorcode


# ---- connect() function ----
db = mysql.connector.connect(
    option_files="wsl.ini"
    )

# ---- Open Cursor ---- 
cursor = db.cursor()

# ---- Consulta de DB
cursor.execute("""
                SELECT DISTINCT 
                                so.type
                                , c.subscriber_id
                                , c.nome
                                , ad.`number`
                                , ad.state  
                FROM service_orders so
                LEFT JOIN addresses ad 
                    ON ad.address_id = so.address_id 
                    AND ad.subscriber_id  = so.subscriber_id 
                LEFT JOIN customer c 
                    ON c.subscriber_id = so.subscriber_id 
                    AND c.address_id = so.address_id 
                WHERE so.`type` IN('Retirada','Instalacao') ORDER BY c.nome""")

dados = cursor.fetchall()

# ---- Lista vazia que irá guardar os registros encontrados
address_change = []

""" 
    i[2] e j[2]-> "nome"
    i[3] e j[3]-> "numero"
"""


for i in dados:
    for j in dados:
        if i[2] == j[2]and i[3] != j[3]:
            address_change.append(i[1])            
            break
        else:
            pass
            
for ocorrencia in address_change:
    print(ocorrencia)


    
# O obejtivo aqui é salvar o resultado em um arquivo csv    
    
#   total_retirada = open('total_retirada.csv', 'a', newline='')
#   
#   gravando = csv.writer(total_retirada) 
#   gravando.writerow(casos)  
