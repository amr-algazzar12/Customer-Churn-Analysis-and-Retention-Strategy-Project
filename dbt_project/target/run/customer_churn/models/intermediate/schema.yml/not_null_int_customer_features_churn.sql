select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select churn
from "churn"."main_intermediate"."int_customer_features"
where churn is null



      
    ) dbt_internal_test