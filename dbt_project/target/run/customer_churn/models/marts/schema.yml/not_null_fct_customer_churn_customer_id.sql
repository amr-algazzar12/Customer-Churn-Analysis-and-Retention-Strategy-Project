select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select customer_id
from "churn"."main_marts"."fct_customer_churn"
where customer_id is null



      
    ) dbt_internal_test