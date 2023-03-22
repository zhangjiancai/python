SELECT student.sname, teach.cname, score.grade
FROM student, score, teach
WHERE student.sno = score.sno AND score.cno = teach.cno AND teach.cname = '数学分析';
