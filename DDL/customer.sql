CREATE TABLE customer(
    customer_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    subscriber_id VARCHAR(15),
    nome VARCHAR(255),
    documento VARCHAR(18),
    email VARCHAR(255),
    celular VARCHAR(15),
    telefone VARCHAR(15),
    produto VARCHAR(15),    
    vencimento VARCHAR(10),
    address_id INT,
    data_criacao TIMESTAMP,
    status_eq CHAR(1),
    plan_value INT,
    usuario_criacao VARCHAR(150),
    parceiro VARCHAR(150),
    FOREIGN KEY (subscriber_id)	REFERENCES addresses(subscriber_id) ON DELETE CASCADE,
    FOREIGN KEY (status_eq)  REFERENCES contract_situation(id_situation)  
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4;