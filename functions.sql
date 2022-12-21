CREATE OR REPLACE FUNCTION get_course_id_by_email(email VARCHAR(20))
RETURNS TABLE(id INTEGER) AS $$
SELECT uc.id
FROM user_course AS uc
INNER JOIN user_student AS s
ON s.id = uc.student_id
$$ LANGUAGE SQL

SELECT * FROM get_course_id_by_email('aman@mail.ru')
