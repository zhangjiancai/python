// ʹ�ñ�׼C���� fopen �� fwrite �����ļ�
#include <stdio.h>
int main()
{
    FILE* fp_w;
    FILE* fp = fopen_s(&fp_w, "test.txt", "w"); // �򿪻򴴽�һ���ļ�
    if (fp == NULL) {
        perror("fopen");
        return -1;
    }
    char buf[] = "Hello, world!";
    int n = fwrite(buf, 1, sizeof(buf), fp); // д�����ݵ��ļ�
    if (n != sizeof(buf)) {
        perror("fwrite");
        return -1;
    }
    fclose(fp); // �ر��ļ�
    return 0;
}