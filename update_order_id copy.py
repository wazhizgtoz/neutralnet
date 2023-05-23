import requests
import sqlite3

def update_order_id(external_id,itype,status,status_appointment):
    conn  = sqlite3.connect('nn.db')
    cursor = conn.cursor()
    cursor.execute(f"""
                       UPDATE service_orders
                       SET type = '{itype}', status = '{status}', status_appointment = '{status_appointment}'
                       WHERE external_id = {external_id};""")
    conn.commit()    
    cursor.close()  