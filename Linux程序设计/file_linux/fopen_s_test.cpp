#include <iostream>
#include <stdlib.h>
using namespace std;
int main()
{
	FILE* fp_w;
	FILE* fp_r;
	//	fp_w = fopen("1.cvs", "a");
	fopen_s(&fp_w, "1.csv", "a");
	//fp_w = fopen_s(&fp_w, "1.csv", "a");
	//if (fp_w == nullptr)
	//{
	//	printf("cuowu")
	//}
	//else {

		for (int i = 0; i < 5; i++)
		{
			fprintf(fp_w, "%d,%d,%d\n", 1, 2, 3);
		}
		fclose(fp_w);
		cout << "д��ɹ���" << endl;


		// ��ȡ
		int num[3]{}, Judge;
		//	fp_r = fopen("1.cvs", "r"); 
		Judge = fopen_s(&fp_r, "1.csv", "r");
		if (Judge == 0)
			cout << "�ļ��򿪳ɹ���" << endl;
		for (int i = 0; i < 5; i++)
		{
			fscanf_s(fp_r, "%d,%d,%d", &num[0], &num[1], &num[2]);
			cout << num[0] << "  " << num[1] << "  " << num[2] << endl;
		}
		fclose(fp_r);
		system("pause");
	}
//}
// a,a+ : û���ļ�������һ�����ļ�����д���ʱ�򲻸���ԭ����Ϣ�� 
// w,w+ : �����Զ�����һ���ļ���д
// r,r+ : �����ļ��������   + �Ŵ����д
