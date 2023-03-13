use teachingdb;
 /****请在此编写代码，操作完毕之后点击评测******/
 
 /**********Begin**********/
  create table student
  (
    sno char(5) PRIMARY KEY,
    sname varchar(20) NOT NULL,
    sdept varchar(20) NOT NULL,
    sclass char(2) NOT NULL,
    ssex char(1);
    birthday DATE;
    totalcredit decimal(4,1);
  )
  
 /**********End**********/
