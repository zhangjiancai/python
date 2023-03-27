// 3-1
#include <stdio.h>
#include <stdlib.h>
int main(void)
{
char c;
FILE *in,*out;
 
if((in = fopen("file.in","r"))==NULL)
{
perror("file open error!");
exit(0);
}
 
out = fopen("file.out","w");
 
while((c = fgetc(in))!=EOF)
fputc(c,out);
 
}
