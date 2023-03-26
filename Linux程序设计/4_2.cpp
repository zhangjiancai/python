// 4-2 
# define STD_INPUT 0					// define standard input
# define STD_OUTPUT 1				// define standard output
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int fd[2];
int pipeline(char* process1,char* process2)
{
int i;

		if ((i=fork())==-1) 			
 		{
			perror("process fork error!");	
			exit(1);
		}
		if (i)
	    {
		      close(fd[0]);					// close input fd of pipe 
		      close(STD_OUTPUT);		// close standard output 1
		      dup(fd[1]);					// redefine 1 as output fd of pipe
		      close(fd[1]);					// close the original output fd of pipe
			  execl(process1, process1, (char*)0);	// use father process to substitute current image
		      printf(" father failed.\n");		// run execl() error
	      }
	      else
	      {
		      close(fd[1]);					// close output fd of pipe
		      close(STD_INPUT);			// close standard input 0
		      dup(fd[0]);					// redefine 0 as input fd of pipe 
		      close(fd[0]);					// close the original input fd of pipe
		      execl(process2,process2,(char*)0);	// use child process to substitute current image
		      printf("child failed.\n");		// run execl() error
	      }
	      exit(2);		
}


int main()
{

static char process1[]="father",process2[]="child";
	 	  
		pipe(fd);						// create pipe
	    pipeline(process1,process2);	
	    exit(1); 
}


