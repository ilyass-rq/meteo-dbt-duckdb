select 
ville , UNNEST((payload->'$.daily.time')::DATE[]) as Dates  ,
UNNEST((payload->'$.daily.temperature_2m_max')::DOUBLE[]) as temp_max ,
UNNEST((payload->'$.daily.temperature_2m_min')::DOUBLE[]) as temp_min 
from {{source('raw', 'raw_meteo')}}
