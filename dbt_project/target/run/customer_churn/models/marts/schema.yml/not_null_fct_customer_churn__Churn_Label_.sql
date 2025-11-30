select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select "Churn Label"
from "churn"."main_marts"."fct_customer_churn"
where "Churn Label" is null



      
    ) dbt_internal_test