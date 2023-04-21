create table contract_situation(
		id_situtation CHAR(1) UNIQUE NOT NULL,
        description VARCHAR(50) UNIQUE NOT NULL        
)ENGINE=INNODB DEFAULT CHARSET=utf8mb4;