select cl.data_criacao
	, cl.subscriber_id as contrato
    , cl.nome
    , cl.documento
    , cl.celular as contato
    , cl. produto
    , cl.vencimento
    , cl.address_id as cod_endereco
    , cs.description as situacao_da_eq
from customer cl 
inner join contract_situation cs
on cs.id_situtation = cl.status_eq
where cl.data_criacao between '2023-04-01 09:00' and '2023-04-20 00:00'
order by cl.data_criacao desc;