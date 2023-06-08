import requests
import mysql.connector


def insert_new_service_order(external_id,type,status,created_at,closed_at,subscriber_id,address_id,work_order_id,schedule_start,schedule_finish,status_appointment):
    db = mysql.connector.connect(option_files="wsl.ini")
    cursor = db.cursor() 
    
    cursor.execute(f"""
                   INSERT INTO redeneutra.service_orders
                    (external_id
                    , type
                    , status
                    , created_at
                    , closed_at
                    , subscriber_id
                    , address_id
                    , work_order_id
                    , schedule_start
                    , schedule_finish
                    , status_appointment) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);""", (external_id
                                                                                    , type
                                                                                    , status
                                                                                    , created_at
                                                                                    , closed_at
                                                                                    , subscriber_id
                                                                                    , address_id
                                                                                    , work_order_id
                                                                                    , schedule_start
                                                                                    , schedule_finish
                                                                                    , status_appointment))
    db.commit()
    cursor.close()
    db.close()



# INSERT INTO redeneutra.service_orders
# (external_id, `type`, status, created_at, closed_at, subscriber_id, address_id, work_order_id, schedule_start, schedule_finish, status_appointment, infra_type, response)
# VALUES('20230526074165', 'Desbloqueio', 'Encerrado', '2023-05-26', '2023-05-26', 'EQ0000000016920', 9144009, '--', '', '', '--', '', NULL);
