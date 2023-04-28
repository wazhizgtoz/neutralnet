CREATE TABLE service_orders(
    external_id VARCHAR(25),
    type VARCHAR(15),
    status VARCHAR(25),
    created_at VARCHAR(10),
    closed_at VARCHAR(10),
    subscriber_id VARCHAR(15),
    address_id INT,
    work_order_id VARCHAR(25),
    schedule_start VARCHAR(16),
    schedule_finish VARCHAR(16),
    status_appointment VARCHAR(50),
    infra_type VARCHAR(50) DEFAULT '',
    response JSON
    -- CONSTRAINT fk_eq_id_customer   FOREIGN KEY (subscriber_id) REFERENCES customer(subscriber_id)       
    -- CONSTRAINT fk_work_order_id_order 	FOREIGN KEY (work_order_id) REFERENCES appointments(work_order_id)
)  ENGINE=InnoDB DEFAULT CHARSET=utf8mb4; 

-- alter table service_orders modify column schedule_finish varchar(16); 