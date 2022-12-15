%第一题
f=[3;2;1];
%aeq=[1,1,1];
a=[1,1,1;1,0,-1;0,1,-1];
b=[6;-4;-3];
[x,y]=linprog(f,a,b,[],[],zeros(3,1));

%第二题
f=[-2;-2];
a=[1,-1;1/2,-1];
b=[-1;-2];
[x,y]=linprog(f,-a,-b,[],[],zeros(2,1));

%第三题
f=[1,-2];
a=[1,1;-1,1;0,-1];
b=[2,1,-3];
[x,y]=linprog(f,-a,-b,[],[],zeros(2,1))



%第四题
function [ X, Z] = myssimplex( A, B, C ,D)
% 单纯形法的实现
% X: 目标函数的最优解
% Z: 目标函数的极小值
% A: 约束函数的系数矩阵
% B: 约束函数的常数列向量
% C: 目标函数的系数向量
% D: 求最大值为1，求最小值为0
% E: 将B，A拼接成新的矩阵
flag = 1;
S=0;
Z=0;
[m, n] = size(A);
BIndex = n - m  + 1 : n;                % 基向量下标集合
    if D==0                             %如果求最小值将C取反
        C=-C;
    end
    if (n < m)
    disp('系数矩阵不符合要求！')
    else
        while flag
            Cb = C(BIndex);             % 基矩阵对应的目标值b
            Zj = (Cb)*A;
            Rj =C-Zj;                   %判别数
            X = zeros(1, n);
            if max(Rj)<=0
            for i=1:m
                   X(BIndex(i))=B(i);
            end
            for i=1:n
                Z=Z+(C(i)*X(i));
            end
               flag = 0;
               fprintf('迭代次数为:%d\n',S);
               disp('已找到最优解：')
               S=0;
               break;
            else
                S=S+1;
                 [~, k1] = max(Rj); %获得换入基变量的位置
                 for i=1:m
                     if A(i,k1)>0
                        P(i)=B(i)/A(i,k1);
                     else 
                        P(i)=inf;
                     end   
                 end
                [~, k2]=min(P);    %获得换出基变量的位置
                BIndex(k2)=k1;     %新的基变量
                E=[B,A];           %B,A合成一个新的矩阵
                E(k2,:)=E(k2,:)/E(k2,k1+1); %将A中k2行，除于A中k2行，k1列；
                for i=1:m                   %更新E
                  if(i==k2)
                      continue;
                  end
                    while(1)
                        E(i,:)= E(i,:)-E(i,k1+1)*E(k2,:);%将E进行初等行换
                        if(E(i,k1+1)==0)
                        break;
                        end
                    end
                    B=E(1:m,1); %E拆开
                    A=E(1:m,2:n+1);
               end
            end
        end
    end
end
A=[2 0 1 0 0 ; 0 1 0 1 0 ;1 2 0 0 1];
B=[4;3;8];
C=[-1 -2 0 0 0];
D=0;
[X,Y]=myssimplex(A,B,C,D)

%第四题
f=[-1;-2];
aeq=[1,0,1,0,0;0,1,0,1,0;1,2,0,0,1];
beq=[4;3,8]
[x,y]=linprog(f,[],[],aeq,beq,zeros(5,1))


%第五题
%min f = 13*x1 + 9*x2+10*x3+11*x4+12*x5+8*x6
%s.t.:x1+x4=400;x2+x5=600;x3+x6=500;0.4*x1+1.1*x2+x3<=800;
        0.5*x4+1.2*x5+1.3*x6<=900;xi>=0,i=1,2,3,4,5,6;
f=[13,9,10,11,12,8];
A=[0.4,1.1,1,0,0,0;0,0,0,0.5,1.2,1.3];
B=[800;900];
aeq=[1,0,0,1,0,0;0,1,0,0,1,0;0,0,1,0,0,1];
beq=[400;600;500];
[x,y]=linprog(f,A,B,aeq,beq,zeros(6,1))

