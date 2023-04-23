/* 
* View para Dashboard Power BI
 * Quantidade de solicitações de instalação por mes e por UF
 * Data 22 de Abril de 2023
 * Author: Washington Silva do Espírito Santo
*/


CREATE OR REPLACE VIEW VWBI_QNT_WORKORDER_INST AS
    SELECT DISTINCT
        UF, DATA_CRIACAO, COUNT(EQINSTALACAO) solicitacao
    FROM
        VW_BCLRN
    WHERE
        TIPO_DE_SERVICO = 'Instalacao'
            AND STATUS_AGENDAMENTO = 'Criado'
    GROUP BY UF , DATA_CRIACAO
    ORDER BY UF ASC;