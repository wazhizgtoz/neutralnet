CREATE TABLE customer(
    customer_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    subscriber_id VARCHAR(15),
    nome VARCHAR(255),
    documento VARCHAR(18),
    celular VARCHAR(15),
    telefone VARCHAR(15),
    produto VARCHAR(15),    
    vencimento VARCHAR(10),
    address_id INT,
    data_criacao TIMESTAMP,
    status_eq CHAR(1),
    FOREIGN KEY (subscriber_id) 
		REFERENCES addresses(subscriber_id) 
			ON DELETE CASCADE     
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4;