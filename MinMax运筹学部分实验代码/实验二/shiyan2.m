%matlab:

f=[3,11,3,10,1,9,2,8,7,4,10,5,3,6,5,6];

aeq=[1 1 1 1 0 0 0 0 0 0 0 0;
     0 0 0 0 1 1 1 1 0 0 0 0;
     0 0 0 0 0 0 0 0 1 1 1 1;
     1 0 0 0 1 0 0 0 1 0 0 0;
     0 1 0 0 0 1 0 0 0 1 0 0;
     0 0 1 0 0 0 1 0 0 0 1 0;
     0 0 0 1 0 0 0 1 0 0 0 1];
beq=[7;4;9;3;6;5;6];
[x,y]=linprog(f,[],[],aeq,beq,zeros(12,1));


!lingo:;
sets:
supplys/1..3/: S;
demands/1..4/: D;
links(supplys, demands): c, x;
endsets
data:
S = 7,4,9;
D = 3,6,5,6;
c = 3 11  3  10
    1  9  2  8
    7  4 10  5;
enddata
min = @sum(links(i,j): c(i,j) * x(i,j));
@for(supplys(i): @sum(demands(j): x(i,j)) = S(i));
@for(demands(j): @sum(supplys(i): x(i,j)) = D(j));


!第二题;
sets:
supplys/1..4/: S;
demands/1..6/: D;
links(supplys, demands): c, x;
endsets
data:
S = 50,60,50,50;
D = 30,20,70,30,10,50;
c = 16 16 13  22  17 17
    14 14 13  19  15 15
    19 19 20  23  M   M
    M  0  M    0   M   0;
enddata
min = @sum(links(i,j): c(i,j) * x(i,j));
@for(supplys(i): @sum(demands(j): x(i,j)) = S(i));
@for(demands(j): @sum(supplys(i): x(i,j)) = D(j));


!第三题;
min=11.25*x1+11.4*x2+11.15*x3+11.3*x4-12.75;
x1>=10;
x1<=25;
x2<=35;
x3<=30;
x4<=10;
x1+x2+x3+x4=70;
@gin(x1);@gin(x2);@gin(x3);@gin(x4);

!第四题;
model:
sets:
variable/1..3/:x;!规定变量;
s_con_num/1..6/:g,dplus,dminus;!软约束条件个数以及相关参数;
s_con(s_con_num,variable):c;!软约束系数;
endsets
data:
g=16000 200 24 12 10 6;
c=500 650 800 6 8 10 0 0 0 1 0 0 0 1 0 0 0 1;
enddata

!min=dminus(1);!第一个目标函数;
!min=dminus(2);!第二个目标函数;
!min=dplus(3);!第三个目标函数;
!min=dminus(4)+dplus(4)+dminus(5)+dplus(5)+dminus(6)+dplus(6);!第四个目标函数;

!2*x(1)+2*x(2)<12;!硬约束；本题没有硬约束;
@for(s_con_num(i):@sum(variable(j):c(i,j)*x(j))+dminus(i)-dplus(i)=g(i));
!软约束表达式;
!dminus(1)=0;!第一级负偏差为0;
!dminus(2)=0;!第二级负偏差为0;
!dplus(3)=0;!第三级正偏差为0;
!dminus(4)+dplus(4)+dminus(5)+dplus(5)+dminus(6)+dplus(6)=0;!这个要去掉;
@for(variable:@gin(x));!限制变量为整数;
end