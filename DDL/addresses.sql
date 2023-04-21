CREATE TABLE addresses(
    address_id INT,
    subscriber_id VARCHAR(15) PRIMARY KEY,	
    street VARCHAR(255),	
    number VARCHAR(10),	
    neighborhood VARCHAR(50),	
    city VARCHAR(50),	
    state VARCHAR(2),	
    postcode INT,	
    complements	VARCHAR(255),
    created_at TIMESTAMP
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;