-- Inserir ordem de instação
INSERT INTO service_orders 
VALUES(1641328,'Instalacao','Criado','2023-04-09 12:59','2023-04-09 12:59','EQ0000000008397',7350000,'SA-872842','2023-04-09 12:59','2023-04-09 12:59','Concluido com sucesso','',NULL);
COMMIT;


-- inserindo ordem de retirada 
INSERT INTO service_orders 
VALUES(1999991,'Retirada','Criado','2023-04-09 13:32','2023-04-09 13:32','EQ0000000008397',7350000,'SA-999998','2023-04-08 13:32','2023-04-08 13:32','Concluido com sucesso','',NULL);
COMMIT;



-- Consultar EQ de Instalação
SELECT subscriber_id, status_eq FROM customer 
WHERE subscriber_id = 'EQ0000000008397';

-- limpando coluna status_eq da tabela customer
UPDATE customer
SET status_eq = ' '
WHERE subscriber_id = 'EQ0000000008397';
COMMIT;



-- Consultando service_orders
SELECT * FROM service_orders 
WHERE subscriber_id = 'EQ0000000008397';



-- Delete service_orders
DELETE FROM service_orders 
WHERE subscriber_id = 'EQ0000000008397'
AND external_id IN(1641328,1999991);
COMMIT ;

SELECT * FROM contract_situation;