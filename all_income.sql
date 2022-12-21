SELECT 
SUM(p.amount) as sum_amount,
uc.language
FROM payments AS p
INNER JOIN user_course AS uc
ON uc.id = p.course_id 
GROUP BY uc.language
