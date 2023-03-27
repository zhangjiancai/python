// 3-4
#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>
 
char buf1[] = "abcdefghij";
char buf2[] = "ABCDEFGHIJ";
 
void err_exit(char *err_s)
{
perror(err_s);
exit(1);
}
 
int main(void)
{
int fd;
 
if((fd = open("hole.file",O_WRONLY|O_CREAT/*|O_APPEND,0644*/)) == -1)
err_exit("file open fail!");
 
if(write(fd,buf1,10)!=10)
err_exit("file write buf1 error!");
 
if(lseek(fd,40,SEEK_SET)==-1)
err_exit("lseek error!");
 
if(write(fd,buf2,10)!=10)
err_exit("file write buf2 error!");
}
