%matlab:
f=[1,1];
intcon=[1,2];
A=[2,5;6,5];
b=[16;30];
[x,y]=intlingprog(-f,intcon,A,b,zeros(2,1));

!lingo:;
min=(-1)*x1+(-1)*x2;
2*x1+5*x2<=16;
6*x1+5*x2<=30;
@gin(x1);@gin(x2);


%第二题
%matlab:
f=[2,-1,5,-3,4];
f=-f;
a=[3,-2,7,-5,-4;1,-1,2,-4,2];
b=[6;0];
intcon=[1:5];
lb=zeros(5,1);
ub=ones(5,1);
[x,y]=intlingprog(f,intcon,a,b,[],[],lb,ub);

!lingo:;
model:
sets:
var/1..5/:x;
var/1,2/:y;
link(var,var):c;!定义集合,以及赋给集合不同的属性名，有点像C语言里面的类class;
endsets
data:
c=3,-2,7,-5,-4
  1,-1,2,-4,2;
y=6 0;

enddata

max=2*x(1)-x(2)+5*x(3)-3*x(4)+4*x(5);
@for(link:@bin(x));

@for(var(i):@sum(var(j):c(i,j)*x(j))<y(i));!Lingo中除了一些特殊的模块，其他的语句均为约束语句;
end

!第三题；
model:
sets:
var/1..5/;
link(var,var):c,x;!定义集合,以及赋给集合不同的属性名，有点像C语言里面的类class;
endsets

data:
c=10 2 3 15 9
    5 10 15 2 4 
    15 5 14 7 15 
    20 15 13 6 8
    0 0 0 0 0 ;!给有属性名的集合赋值;
enddata

min=@sum(link:c*x);!目标函数，Lingo中识别目标函数是用max和min来，所以目标函数语句写在哪都可;
@for(link:@bin(x));
@for(var(i):@sum(var(j):x(i,j))=1); !Lingo中除了一些特殊的模块，其他的语句均为约束语句;
@for(var(j):@sum(var(i):x(i,j))=1);
end

%第四题
m=1;
A=[0 5 15 40 80 90];
B=[0 5 15 40 60 70];
C=[0 4 26 40 45 50];
for i=1:6
    for j=1:6
        for k=1:6
            if i+j+k==8
                d(m)=A(i)+B(j)+C(k);
                E(m,1)=i;
                E(m,2)=j;
                E(m,3)=k;
                m=m+1;
            else
                continue;
            end
        end
    end
end 
MAXNum=d(1);
for l=1:size(d,2);
    if d(l)>MAXNum
        MAXNum=d(l);
        p=l;
    else
        continue;
    end
end
for l=1:size(d,2)
    if d(l)==MAXNum
        E(l,:)
    else
        continue;
    end
end
MAXNum

                