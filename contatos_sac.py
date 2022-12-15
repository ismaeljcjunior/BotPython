import pyodbc
import pandas as pd
import dotenv
import os
dotenv.load_dotenv(dotenv.find_dotenv())

cnxn = pyodbc.connect(os.getenv("DBA_STRING"))

cursor = cnxn.cursor()

data = pd.read_sql_query("Select distinct O.ID_ORDEM  as NUM_OS ,O.ABERTURA AS DATA_OS_ABERTA ,c.FANTASIA ,t.NM_COLABORADOR as ROTA_TECNICO_RESPONSAVEL ,CAST(O.TX_OBSERVACOES_CLIENTE as nvarchar (max)) as INFORMAÇÕES_ADICIONAIS ,SOLU.DESCRICAOSOLUCAO as SOLUCAO from dbORDEM o LEFT JOIN dbPROVIDENCIA prov on prov.CD_CLIENTE = o.CD_CLIENTE LEFT JOIN dbCENTRAL c on c.CD_CLIENTE = o.CD_CLIENTE  LEFT JOIN OS_SOLICITANTE S on S.CD_OS_SOLICITANTE = o.CD_OS_SOLICITANTE LEFT JOIN OSSOLUCAO SOLU on SOLU.IDOSSOLUCAO = O.IDOSSOLUCAO LEFT JOIN COLABORADOR T on T.CD_COLABORADOR = O.ID_INSTALADOR where 1=1 and o.FECHADO = 1  and o.ABERTURA between CURRENT_TIMESTAMP -1 and CURRENT_TIMESTAMP and SOLU.DESCRICAOSOLUCAO like '%ATENDIMENTO PRESENCIAL%' AND t.NM_COLABORADOR  IN ('CPR 01 - RONALDO DIAS','CPR 02 - FABIANO NEVES','CPR 03 – RENAN PEREIRA','CPR 04– EDUARDO BESSA','CPR 06 - DANYEL','CPR 09 – JHONNATHAN ROBERT','CPR 10 - JAMES','CPR 12 - RUBIAN','CPR 24H – JONE WESLEY','CPR DEPARTAMENTO TÉCNICO TRIAGEM') AND t.NM_COLABORADOR in ('ROTA 03 - ROMERSON','ROTA 06 - MARIO SERGIO','ROTA 07 - JOAO FILHO','ROTA 08 - LEVI','ROTA 09 - Rodrigo Vieira','ROTA 12 - ATILA VINICIUS') order by DATA_OS_ABERTA desc",cnxn)
print(type(data))

data.to_excel('Contatos_SAC.xls')

