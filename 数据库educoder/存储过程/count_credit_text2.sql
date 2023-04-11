DELIMITER $$
CREATE FUNCTION count_credit(sno VARCHAR(10)) RETURNS INT
BEGIN

DECLARE @total_credit INT DEFAULT 0;


DECLARE @score INT;
DECLARE @cno INT;

DECLARE cur CURSOR 
FOR SELECT cno,grade FROM score 
WHERE sno = sno;

OPEN cur 

FETCH NEXT FROM cur INTO @cno,@score;
while @@fetch_status=0
BEGIN
    CREATE TABLE #TEST(cno int )
    EXEC('insert #TEST select credit from course where cno = cno' +  score);
    DECLARE @course_credit INT;
    declare cur_2 CURSOR FOR (select credit from #TEST)
    open cur_2
    FETCH NEXT FROM cur_2 INTO @course_credit;
    while @@fetch_status=0
        BEGIN
        IF (grade >= 60) THEN
            SET total_credit = total_credit + course_credit;
        END IF;

        End
END
CLOSE cur;
DEALLOCATE cur;
RETURN total_credit;
END$$

DELIMITER ;