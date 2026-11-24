select ville, date_meteo,temperature_max, temperature_min 
from {{ref('stg_meteo')}}
where temperature_max < temperature_min