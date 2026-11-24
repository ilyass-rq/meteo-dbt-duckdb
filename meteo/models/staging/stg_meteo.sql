SELECT 
ville , UNNEST((payload->'$.daily.time')::DATE[]) as date_meteo  ,
UNNEST((payload->'$.daily.temperature_2m_max')::DOUBLE[]) as temperature_max ,
UNNEST((payload->'$.daily.temperature_2m_min')::DOUBLE[]) as temperature_min 
FROM {{source('raw', 'raw_meteo')}}
