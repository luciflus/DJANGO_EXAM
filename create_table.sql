CREATE TABLE payments
(
	id SERIAL PRIMARY KEY,
	Course_id INTEGER,
	Amount INTEGER,
	Pay_date DATE NOT NULL, 
	FOREIGN KEY(course_id) REFERENCES user_course (id) ON DELETE CASCADE
);