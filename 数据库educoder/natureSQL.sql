/*
SELECT s.name, c.course_name, t.teacher_name, sc.score
FROM student s
INNER JOIN score sc ON s.student_id = sc.student_id
INNER JOIN course c ON sc.course_id = c.course_id
INNER JOIN teacher t ON c.teacher_id = t.teacher_id
WHERE c.course_name = '数学分析' AND t.teacher_name = '严敏' AND sc.is_elective = 1;
*/
/*
SELECT s.sname, c.cname, t.tname, g.grade
FROM students s
NATURAL JOIN courses c
NATURAL JOIN teachers t
NATURAL JOIN grades g
WHERE c.cname = '数学分析' AND t.tname = '严敏'
*/
/*
SELECT student.sname,course.cname,course.tname,grade.grade
FROM student 
*/

/*INNER JOIN student*/

/*
INNER JOIN course
INNER JOIN grade
WHERE course.cname = '数学分析' AND course.tname = '严敏';
*/

SELECT a.sname,b.cname,d.tname,c.grade 

FROM student a 
NATURAL JOIN score c 
NATURAL JOIN course b 
NATURAL JOIN teach d
WHERE  cname='数学分析' AND tname='严敏';