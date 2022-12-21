SELECT 
uc.name,
uc.date_started,
us.name,
um.name,
uc.language
FROM user_course AS uc
INNER JOIN user_student AS us
ON us.id = uc.student_id
INNER JOIN user_mentor AS um
ON um.id = uc.mentor_id

