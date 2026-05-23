SELECT 
    employee_id,
    CASE 
        WHEN name not like 'M%' and employee_id % 2 != 0 THEN 0
        ELSE salary
    END AS bonus
FROM employees;