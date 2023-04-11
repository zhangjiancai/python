use teachingdb;
 /****请在此编写代码，操作完毕之后点击评测******/
 /**********Begin**********/
DELIMITER $$
DROP FUNCTION IF EXISTS count_credit$$
CREATE  FUNCTION count_credit(stuno CHAR(6)) RETURNS INT
    READS SQL DATA
BEGIN
      DECLARE stucno CHAR(3) ;    
      DECLARE cred INT DEFAULT 0;
      DECLARE t_cred INT DEFAULT 0;
      DECLARE  done INT DEFAULT FALSE;
      DECLARE stucur CURSOR FOR SELECT cno FROM score WHERE sno=stuno AND grade>=60;
      DECLARE CONTINUE HANDLER FOR NOT FOUND SET done=TRUE;
      OPEN stucur;
      loop_cursor:LOOP
           FETCH stucur INTO stucno;
           IF done THEN LEAVE loop_cursor; END IF;
           SELECT credit INTO cred FROM course WHERE cno=stucno;
           SET t_cred=t_cred+cred;    
      END LOOP;
      RETURN  t_cred;
    END$$
DELIMITER ;
 /**********End**********/

  /**********
  -- 切换到数据库 teachingdb
USE teachingdb;

-- 设置 DELIMITER，将默认的分号 ; 改成 $$
DELIMITER $$

-- 如果函数 count_credit 已存在，先将其删除
DROP FUNCTION IF EXISTS count_credit$$

-- 创建函数 count_credit，输入参数为学生学号，返回值为 INT 类型的总学分
CREATE FUNCTION count_credit(stuno CHAR(6)) RETURNS INT
    READS SQL DATA
BEGIN
    -- 定义变量 stucno，用于存储查询到的课程编号
    DECLARE stucno CHAR(3) ;
    -- 定义变量 cred，用于存储查询到的课程学分
    DECLARE cred INT DEFAULT 0;
    -- 定义变量 t_cred，用于存储总学分，初始值为 0
    DECLARE t_cred INT DEFAULT 0;
    -- 定义变量 done，用于标记游标是否读取完毕，初始值为 FALSE
    DECLARE  done INT DEFAULT FALSE;
    -- 声明游标 stucur，用于查询学生选修的所有课程编号
    DECLARE stucur CURSOR FOR SELECT cno FROM score WHERE sno=stuno AND grade>=60;
    -- 定义 CONTINUE HANDLER，用于处理游标未读取到记录的情况
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done=TRUE;
    -- 打开游标 stucur
    OPEN stucur;
    -- 定义一个无限循环 loop_cursor，用于读取游标 stucur 中的数据
    loop_cursor:LOOP
        -- 从游标 stucur 中获取一条记录，存储到变量 stucno 中
        FETCH stucur INTO stucno;
        -- 如果游标已经读取完所有记录，则跳出循环
        IF done THEN LEAVE loop_cursor; END IF;
        -- 根据课程编号 stucno 查询该课程的学分，存储到变量 cred 中
        SELECT credit INTO cred FROM course WHERE cno=stucno;
        -- 累加课程学分到总学分变量 t_cred 中
        SET t_cred=t_cred+cred;    
    END LOOP;
    -- 返回总学分
    RETURN  t_cred;
END$$

-- 恢复 DELIMITER 为默认值 ;
DELIMITER ;

  **********/