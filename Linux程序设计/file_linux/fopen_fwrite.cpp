// 使用标准C函数 fopen 和 fwrite 操作文件
#include <stdio.h>
int main()
{
    FILE* fp_w;
    FILE* fp = fopen_s(&fp_w, "test.txt", "w"); // 打开或创建一个文件
    if (fp == NULL) {
        perror("fopen");
        return -1;
    }
    char buf[] = "Hello, world!";
    int n = fwrite(buf, 1, sizeof(buf), fp); // 写入数据到文件
    if (n != sizeof(buf)) {
        perror("fwrite");
        return -1;
    }
    fclose(fp); // 关闭文件
    return 0;
}