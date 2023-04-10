 use teachingdb;
 /****请在此编写代码，操作完毕之后点击评测******/
 
 /**********Begin**********/
DELIMITER $$
/*--DELIMITER 是 MySQL 命令行客户端中的一个指令，它可以改变语句结束符号，让 MySQL 命令行客户端不再将分号 ; 当做语句结束符号。这样在定义存储过程等多语句的情况下，可以正确地将多个语句一起执行。*/
DROP PROCEDURE IF EXISTS pro_findname$$
/*--这是一个 SQL 语句，用于删除名为 pro_findname 的存储过程，如果这个存储过程不存在则不会有任何影响。*/
CREATE PROCEDURE pro_findname(in word char(3))
BEGIN
           select * from student where sname like concat('%',word,'%');
    END$$
DELIMITER ;

 /**********End**********/
