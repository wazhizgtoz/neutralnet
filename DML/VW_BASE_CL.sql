CREATE OR REPLACE VIEW VW_BCLRN AS
    SELECT 
        CONCAT('EQ00000000000', eq.customer_id) AS CHAVE,
        address.state AS UF,
        eq.subscriber_id AS EQINSTALACAO,
        UPPER(eq.nome) AS NOME_CLIENTE,
        eq.documento AS CPF,
        os.status_appointment AS STATUS_AGENDAMENTO,
        eq.produto AS PRODUTO,
        DATE_FORMAT(eq.data_criacao, '%d/%m/%Y') AS DATA_CRIACAO,
        DATE_FORMAT(os.schedule_finish, '%d/%m/%Y') AS DATA_AGENDAMENTO,
        os.work_order_id AS WORKORDER,
        os.type AS TIPO_DE_SERVICO,
        cs.description AS STATUS_FIM
    FROM
        customer eq
            JOIN
        addresses address ON address.address_id = eq.address_id
            AND address.subscriber_id = eq.subscriber_id
            JOIN
        contract_situation cs ON id_situation = eq.status_eq
            JOIN
        service_orders os ON os.subscriber_id = eq.subscriber_id
    ORDER BY 1;




