CREATE TABLE IF NOT EXISTS students (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    fullname TEXT NOT NULL,
    birth_year INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS grades (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    subject TEXT NOT NULL,
    grade INTEGER NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE
);

INSERT INTO students (fullname, birth_year) VALUES
        ('Alice Johnson',2005),
        ('Brian Smith',2004),
        ('Carla Reyes',2006),
        ('Daniel Kim',2005),
        ('Eva Thompson',2003),
        ('Felix Nguyen',2007),
        ('Grace Patel',2005),
        ('Henry Lopez',2004),
        ('Isabella Martinez',2006);

INSERT INTO grades (student_id, subject, grade) VALUES
        (1, 'Math', 88),
        (1,'English', 92),
        (1, 'Science', 85),
        (2, 'Math', 75),
        (2, 'History', 83),
        (2, 'English', 79),
        (3, 'Science', 95),
        (3, 'Math', 91),
        (3, 'Art', 89),
        (4, 'Math', 84),
        (4, 'Science', 88),
        (4, 'Physical Education', 93),
        (5, 'English', 90),
        (5, 'History', 85),
        (5, 'Math', 88),
        (6, 'Science', 72),
        (6, 'Math', 78),
        (6, 'English', 81),
        (7, 'Art', 94),
        (7, 'Science', 87),
        (7, 'Math', 90),
        (8, 'History', 77),
        (8, 'Math', 83),
        (8, 'Science', 80),
        (9, 'English', 96),
        (9, 'Math', 89),
        (9, 'Art', 92);

SELECT grades.*
FROM grades
JOIN students ON grades.student_id = students.id
WHERE students.fullname = 'Alice Johnson';

SELECT AVG(grade) AS average_grade
FROM grades;

SELECT *
FROM students
WHERE birth_year > 2004;

SELECT subject, AVG(grade) AS avr_grade
FROM grades
GROUP BY subject;

SELECT students.fullname,
       AVG(grades.grade) AS avg_grades
FROM grades
JOIN students ON grades.student_id = students.id
GROUP BY students.id
ORDER BY avg_grades DESC
LIMIT 3;

SELECT DISTINCT students.fullname
FROM students
JOIN grades ON students.id = grades. student_id
WHERE grades.grade < 80;

