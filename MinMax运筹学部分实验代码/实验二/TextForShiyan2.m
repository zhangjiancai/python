clc
f=[2 9 10 7 1 3 4 2 8 4 2 5]';
intcon=[1 2 3 4 5 6 7 8 9 10 11 12];
A=[];
b=[];
Aeq=[1 1 1 1 0 0 0 0 0 0 0 0;
     0 0 0 0 1 1 1 1 0 0 0 0;
     0 0 0 0 0 0 0 0 1 1 1 1;
     1 0 0 0 1 0 0 0 1 0 0 0;
     0 1 0 0 0 1 0 0 0 1 0 0;
     0 0 1 0 0 0 1 0 0 0 1 0;
     0 0 0 1 0 0 0 1 0 0 0 1];
 beq=[9;5;7;3;8;4;6];
 lb=[0 0 0 0 0 0 0 0 0 0 0 0 ];
x=reshape(x,4,3);
 x=x'
 yunfei
 [x,yunfei2]=linprog(f,A,b,Aeq,beq,lb);

 clc
f=[2 9 10 7 1 3 4 2 8 4 2 5]';
%intcon=[1 2 3 4 5 6 7 8 9 10 11 12];
A=[];
b=[];
Aeq=[1 1 1 1 0 0 0 0 0 0 0 0;
     0 0 0 0 1 1 1 1 0 0 0 0;
     0 0 0 0 0 0 0 0 1 1 1 1;
     1 0 0 0 1 0 0 0 1 0 0 0;
     0 1 0 0 0 1 0 0 0 1 0 0;
     0 0 1 0 0 0 1 0 0 0 1 0;
     0 0 0 1 0 0 0 1 0 0 0 1];
beq=[9;5;7;3;8;4;6];
lb=[0 0 0 0 0 0 0 0 0 0 0 0 ];
%x=reshape(x,4,3);
% x=x'
%yunfei
[x,yunfei2]=linprog(f,A,b,Aeq,beq,lb);
x
yunfei2


model:
sets:
variable/1..2/:x;!规定变量;
s_con_num/1..4/:g,dplus,dminus;!软约束条件个数以及相关参数;
s_con(s_con_num,variable):c;!软约束系数;
endsets
data:
g=1500 0 16 15;
c=200 300 2 -1 4 0 0 5;
enddata
min=dminus(1);!第一个目标函数;
2*x(1)+2*x(2)<12;!硬约束;
@for(s_con_num(i):@sum(variable(j):c(i,j)*x(j))+dminus(i)-dplus(i)=g(i));
!软约束表达式;
@for(variable:@gin(x));!限制变量为整数;
end