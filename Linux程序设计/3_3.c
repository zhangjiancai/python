// 3-3
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
FILE *fp;
 
if((fp = fopen("hole.file","w")) == NULL)
err_exit("file open fail!");
 
if(fwrite(buf1,sizeof(buf1),1,fp)!=1)
err_exit("file write buf1 error!");
 
if(fseek(fp,40,SEEK_SET)==-1)
err_exit("fseek error!");
 
if(fwrite(buf2,strlen(buf2),1,fp)!=1)
err_exit("file write buf2 error!");
 
fclose(fp);
}
