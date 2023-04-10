DELIMITER $$
CREATE FUNCTION count_credit(sno VARCHAR(10)) RETURNS INT
BEGIN
    DECLARE total_credit INT DEFAULT 0;
    DECLARE course_credit INT;
    DECLARE score INT;
    
    DECLARE cur_2 CURSOR
    FOR SELECT credit FROM course
    WHERE cno = cno ;

    DECLARE cur CURSOR 
    FOR SELECT cno,grade FROM score 
    WHERE sno = sno;
    
    OPEN cur;
    read_loop: LOOP
        
        FETCH cur INTO sno, score;
        FETCH cur_2 INTO course_credit;
        IF (grade >= 60) THEN
            SET total_credit = total_credit + course_credit;
        END IF;
        IF (FETCH_STATUS = 0) THEN
            ITERATE read_loop;
        END IF;
        LEAVE read_loop;
    END LOOP;
    CLOSE cur;
    
    RETURN total_credit;
END$$
DELIMITER ;

-------------------------------------
declare @变量1 varchar(max)
declare @变量2 varchar(max)
DECLARE ProvinceCursor CURSOR FOR  (select 字段1,字段2 from 表名)
open ProvinceCursor
FETCH NEXT FROM ProvinceCursor INTO @变量1,@变量2;  
while @@fetch_status=0
BEGIN
    CREATE TABLE #TEST (字段1 int)   --创建临时表#TEST
    --把符合情况的客户id加入临时表
    EXEC('insert #TEST select 字段 from 表 where 字段2='+变量2+' ' + 变量1); --拼接出sql语句  注：变量1是一个查询条件
    declare @变量3 varchar(max) --声明变量3
    --游标2，遍历
    DECLARE ProvinceCursor2 CURSOR FOR  (select 字段1 from #TEST)
    --打开游标
    open ProvinceCursor2 
    --移动游标，加载数据
    FETCH NEXT FROM ProvinceCursor2 INTO @变量3;
    while @@fetch_status=0
           BEGIN
           --操作
           Print @变量3
           End
END
CLOSE ProvinceCursor;
DEALLOCATE ProvinceCursor;

--------------------------------------------------
