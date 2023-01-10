//~~~~~~~~~~~~~~~~~~~
//头文件区
//~~~~~~~~~~~~~~~~~~~
#include <stdio.h>
#include "scheduler.h"

//~~~~~~~~~~~~~~~~~~~
//接口定义区
//~~~~~~~~~~~~~~~~~~~
#define MAX_TASKS 10
static volatile unsigned char cur_task_num = 0;

//~~~~~~~~~~~~~~~~~~~
//变量定义区
//~~~~~~~~~~~~~~~~~~~
static running_queue_def running_queue[MAX_TASKS] = {0};

//~~~~~~~~~~~~~~~~~~~
//函数定义区
//~~~~~~~~~~~~~~~~~~~
int create_task(const void (*fun)(),unsigned short period)
{
    unsigned char i;
    
    if(cur_task_num >= MAX_TASKS)
    {
        printf ("over limit max_tasks\n");
        return -1;

    }
    
    running_queue[i].fun = fun;
    running_queue[i].period
}