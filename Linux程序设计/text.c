#include <stdio.h>

int main ()
{
   FILE *fp;

   /* 首先重命名文件 */
   rename("file.txt", "newfile.txt");

   /* 现在让我们尝试打开相同的文件 */
   fp = fopen("file.txt", "r");
   if( fp == NULL ) {
      perror("Error: ");
      return(-1);
   }
   fclose(fp);
      
   return(0);
}
