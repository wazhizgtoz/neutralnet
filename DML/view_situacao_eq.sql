SELECT a.subscriber_id,
    c.nome,
    c.celular,
    c.produto,
    a.postcode,
    a.number,
    a.city,
    a.state,
    s.external_id,
    s.type,
    s.status,
    s.work_order_id,
    s.status_appointment,
    s.created_at,
    c.status_eq AS "SITUACAO EQ"
FROM service_orders s
    LEFT JOIN addresses a ON a.address_id = s.address_id
    AND a.subscriber_id = s.subscriber_id
    INNER JOIN customer c ON c.address_id = s.address_id
    AND c.subscriber_id = s.subscriber_id
WHERE s.status_appointment in('Concluido com sucesso', 'Criado')
AND s.subscriber_id = 'EQ0000000008397';


