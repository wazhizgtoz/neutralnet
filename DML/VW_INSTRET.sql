create or replace view VW_INSTRET as
select distinct *
from VW_BCLRN
where tipo_de_servico = 'Instalacao'
    and status_agendamento = 'Concluído com sucesso'
    and status_fim = 'Instalado'
union all
select distinct *
from VW_BCLRN
where tipo_de_servico = 'Retirada'
    and status_agendamento = 'Concluído com sucesso'
    and status_fim = 'Inativo'
order by eqinstalacao;