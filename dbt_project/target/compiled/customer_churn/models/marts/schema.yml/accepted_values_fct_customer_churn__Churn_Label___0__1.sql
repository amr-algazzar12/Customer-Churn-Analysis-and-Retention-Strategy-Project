
    
    

with all_values as (

    select
        "Churn Label" as value_field,
        count(*) as n_records

    from "churn"."main_marts"."fct_customer_churn"
    group by "Churn Label"

)

select *
from all_values
where value_field not in (
    '0','1'
)


