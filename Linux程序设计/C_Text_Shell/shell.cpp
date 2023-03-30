#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <sys/wait.h>

#define MAX_LINE 80 /* 命令行的最大长度 */

int main(void)
{
    char *args[MAX_LINE / 2 + 1]; /* 用于保存输入的命令 */
    int should_run = 1; /* 标记是否退出程序 */
    int background = 0; /* 标记是否在后台运行 */
    pid_t pid; /* 用于保存fork返回的进程ID */
    int status; /* 用于保存waitpid返回的状态 */

    while (should_run) {
        printf("osh> ");
        fflush(stdout);

        char command[MAX_LINE]; /* 用于保存输入的命令 */
        fgets(command, MAX_LINE, stdin); /* 读取命令 */

        int i = 0;
        args[i] = strtok(command, " \n"); /* 将命令按空格或换行符分割成一个个参数 */

        while (args[i] != NULL) { /* 将所有参数存到args数组中 */
            i++;
            args[i] = strtok(NULL, " \n");
        }

        if (args[0] == NULL) { /* 如果没有输入任何参数，继续等待输入 */
            continue;
        }

        if (strcmp(args[i-1], "&") == 0) { /* 如果最后一个参数是&，表示在后台运行 */
            background = 1;
            args[i-1] = NULL; /* 去掉&符号 */
        }

        pid = fork(); /* 创建子进程 */

        if (pid < 0) { /* 如果fork出错，输出错误信息并退出程序 */
            fprintf(stderr, "Fork failed");
            return 1;
        } else if (pid == 0) { /* 如果是子进程 */
            if (execvp(args[0], args) == -1) { /* 执行命令 */
                fprintf(stderr, "Error executing command\n"); /* 如果出错，输出错误信息 */
                return 1;
            }
            exit(0);
        } else { /* 如果是父进程 */
            if (!background) { /* 如果不是后台运行，等待子进程结束 */
                waitpid(pid, &status, 0);
            }
        }

        background = 0; /* 重置标记 */
    }

    return 0;
}