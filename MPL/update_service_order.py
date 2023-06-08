import requests
import mysql.connector
from mysql.connector import errorcode


def update_status(status,status_appointment,closed_at,external_id):
    db = mysql.connector.connect(option_files="wsl.ini")
    cursor = db.cursor()     
    cursor.execute(f"""
                    UPDATE service_orders
                    SET status = '{status}', status_appointment = '{status_appointment}', closed_at = '{closed_at}'
                    WHERE external_id = {external_id};
                    """)
    db.commit()    
    cursor.close()
    db.close() 