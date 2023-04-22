CREATE OR REPLACE VIEW VW_BCLRN
AS
select  CONCAT('EQ00000000000', eq.customer_id) AS CHAVE
	  , address.state as UF
	  , eq.subscriber_id as EQINSTALACAO
      , UPPER(eq.nome) as NOME_CLIENTE
      , eq.documento as CPF
      , os.status_appointment as STATUS_AGENDAMENTO      
      , eq.produto as PRODUTO      
      , DATE_FORMAT(eq.data_criacao,      "%d/%m/%Y") as DATA_CRICAO
      , DATE_FORMAT(os.schedule_finish,   "%d/%m/%Y") as DATA_AGENDAMENTO
      , os.work_order_id as git branch
      , os.type as TIPO_DE_SERVIÇO      
      , cs.description as STATUS_FIM
      
from customer eq
join addresses address on address.address_id = eq.address_id and address.subscriber_id = eq.subscriber_id
join contract_situation cs on id_situation = eq.status_eq
join service_orders os on os.subscriber_id = eq.subscriber_id
order by 1;


