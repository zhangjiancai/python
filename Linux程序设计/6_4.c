#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#define SHMSZ 27
int main(void)
{
	int shmid;
	key_t key;
	char *shm,*s;

	key = 1234;
	if((shmid = shmget(key,SHMSZ,0666)) < 0){
		perror("shmget error!");
		exit(0);
	}
	if((shm = shmat(shmid,NULL,0)) == (char *)-1){
		perror("shmat error!");
		exit(0);
	}
	//for(s = shm; *s != NULL; s++)
    for(s = shm; *s != '\0'; s++)
		putchar(*s);
	putchar('\n');
	*shm = '*';
	exit(0);
}
