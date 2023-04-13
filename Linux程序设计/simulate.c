#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <signal.h>
#include <string.h>
#include <semaphore.h>

sem_t empty;
sem_t full;

FILE *fp;

void *write_thread(void *id){
    int x;

    srand(getpid());
    while(1) {
       x = rand()%5;
       sleep(x);
       sem_wait(&empty);
       fprintf(fp, "thread %d write %d in log.file\n", (int)id, x);
       sem_post(&full);
    }
}

void termination_handler(int signum) {
    sem_destroy(&empty);
    sem_destroy(&full);
    fclose(fp);
    exit(0);
}

int main(){
    pthread_t write_th[5];
    pthread_attr_t thread_attr;
    int i = 0;
    int offset = 0;
    int res;
    char buf[256];

    sem_init(&empty, 0, 1);
    sem_init(&full, 0, 0);
    signal(SIGINT, termination_handler);

    memset(buf,'\0', sizeof(buf));

    if((fp = fopen("./log.file","a+")) == NULL) {
        perror("file log.file open error!");
        exit(1);
    }


    res = pthread_attr_init(&thread_attr);
    if (res != 0) {
        perror("Attribute creation failed");
        exit(EXIT_FAILURE);
    }
    res = pthread_attr_setdetachstate(&thread_attr, PTHREAD_CREATE_DETACHED);
    if (res != 0) {
        perror("Setting detached attribute failed");
        exit(EXIT_FAILURE);
    }

    for(; i<5; i++) {
        res = pthread_create(&write_th[i], &thread_attr, write_thread, (void *)i);
        if (res != 0) {
  	    perror("thread create error!\n");
	    exit(1);
	}
    }

   for(;;) {
       sem_wait(&full);
       fseek(fp, offset*strlen(buf), SEEK_SET);
       memset(buf,'\0', sizeof(buf));
       fgets(buf, sizeof(buf), fp);
       offset++;
       printf("read from file: %s\n", buf);
       sem_post(&empty);
   }
}
