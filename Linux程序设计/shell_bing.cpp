// 一个简单的shell框架代码
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>

#define MAXLINE 1024 // 输入最大长度
#define MAXARGS 128 // 参数最大个数

// 从标准输入读取一行命令
int read_command(char *cmdline) {
    if (fgets(cmdline, MAXLINE, stdin) == NULL) {
        return -1; // 读取失败或到达文件尾
    }
    return 0; // 读取成功
}

// 解析命令行，将参数存入argv数组
void parse_command(char *cmdline, char **argv) {
    char *delim = " \t\n"; // 分隔符
    char *token; // 每个参数
    int argc = 0; // 参数个数

    token = strtok(cmdline, delim); // 第一个参数
    while (token != NULL) {
        argv[argc++] = token; // 存入数组
        token = strtok(NULL, delim); // 下一个参数
    }
    argv[argc] = NULL; // 最后一个元素置空
}

// 执行命令，如果是内部命令则直接处理，如果是外部命令则创建子进程执行
void execute_command(char **argv) {
    pid_t pid; // 进程ID

    if (argv[0] == NULL) {
        return; // 空命令直接返回
    }

    // 处理内部命令，这里只实现了exit和cd两个例子，您可以添加更多的内部命令
    if (strcmp(argv[0], "exit") == 0) {
        exit(0); // 退出shell
    }
    if (strcmp(argv[0], "cd") == 0) {
        if (chdir(argv[1]) < 0) {
            perror("cd"); // 切换目录失败，打印错误信息
        }
        return; // 完成内部命令，返回
    }

    // 处理外部命令，创建子进程执行
    pid = fork(); // 创建子进程
    if (pid < 0) {
        perror("fork"); // 创建失败，打印错误信息
        exit(1);
    }
    if (pid == 0) {
        // 子进程执行外部命令
        if (execvp(argv[0], argv) < 0) {
            perror("execvp"); // 执行失败，打印错误信息
            exit(1);
        }
    }
    // 父进程等待子进程结束
    wait(NULL);
}

int main() {
    char cmdline[MAXLINE]; // 命令行字符串
    char *argv[MAXARGS]; // 参数数组

    while (1) {
        printf("myshell> "); // 打印提示符
        if (read_command(cmdline) < 0) {
            break; // 读取失败或到达文件尾，退出循环
        }
        parse_command(cmdline, argv); // 解析命令行
        execute_command(argv); // 执行命令
    }

    return 0;
}