import mysql.connector
from mysql.connector import errorcode
import csv

with open('addresses20042023.csv', 'r') as f:
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
    address_id = row[0]
    subscriber_id = row[1]	
    street = row[2]	
    number = row[3]	
    neighborhood = row[4]	
    city = row[5]		
    state = row[6]	
    postcode = row[7]	
    complements	= row[8]
    created_at = row[9]
    cursor.execute("""
                   INSERT INTO addresses(address_id,
                        subscriber_id,	
                        street,	
                        number,	
                        neighborhood,	
                        city,	
                        state,	
                        postcode,	
                        complements,
                        created_at) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (address_id,
                        subscriber_id,	
                        street,	
                        number,	
                        neighborhood,	
                        city,	
                        state,	
                        postcode,	
                        complements,
                        created_at))
db.commit()

# --- Fechando conexão --- 
cursor.close()

db.close()  