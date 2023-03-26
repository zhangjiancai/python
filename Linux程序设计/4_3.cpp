#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int fd[2];

int main()
{
static char string[] = "arent is using pipe write." ;
        int len;
		len = sizeof(string) ;
        write(fd[1], string, len) ;			// write string into the pipe
        printf("parent, parent, parent \n \n \n" ) ;
        exit(0) ;
}

