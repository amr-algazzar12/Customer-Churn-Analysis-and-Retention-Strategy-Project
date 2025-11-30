
    
    

with all_values as (

    select
        gender_encoded as value_field,
        count(*) as n_records

    from "churn"."main_intermediate"."int_customer_features"
    group by gender_encoded

)

select *
from all_values
where value_field not in (
    '0','1'
)


