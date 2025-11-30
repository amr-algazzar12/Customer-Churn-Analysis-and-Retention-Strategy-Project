select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select tenure_months
from "churn"."main_staging"."stg_customers"
where tenure_months is null



      
    ) dbt_internal_test