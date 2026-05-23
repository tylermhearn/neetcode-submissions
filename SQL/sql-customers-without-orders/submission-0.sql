-- Write your query below
select name 
from customers 
left join orders on orders.customer_id = customers.id 
