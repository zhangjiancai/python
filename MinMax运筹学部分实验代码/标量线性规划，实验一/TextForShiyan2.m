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