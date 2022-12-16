openExample('optim/SolveanMILPwithLinearInequalitiesExample')

包含整数变量下标的向量，顾名思义，就是你的规划变量{x1，x2，x3，...，xn}，其中哪一项是整数，intcon里就加上哪一项。如x2，x3是整数，intcon=[2 3]。

model:
sets:
var/1,2/:x,y;
link(var,var):a;!定义集合,以及赋给集合不同的属性名，有点像C语言里面的类class;
endsets

data:
a=9 7 
  7 20;
y=56 70;!给有属性名的集合赋值;
enddata

max=40*x(1)+90*x(2);!目标函数，Lingo中识别目标函数是用max和min来，所以目标函数语句写在哪都可;
@for(var:@gin(x));
@for(var(i):@sum(var(j):a(i,j)*x(j))<y(i));!Lingo中除了一些特殊的模块，其他的语句均为约束语句;
end

model:
sets:
var/1..5/;
link(var,var):c,x;!定义集合,以及赋给集合不同的属性名，有点像C语言里面的类class;
endsets

data:
c=3 8 2 10 3 
  8 7 2 9 7 
  6 4 2 7 5
  8 4 2 3 5
  9 10 6 9 10;!给有属性名的集合赋值;
enddata

min=@sum(link:c*x);!目标函数，Lingo中识别目标函数是用max和min来，所以目标函数语句写在哪都可;
@for(link:@bin(x));
@for(var(i):@sum(var(j):x(i,j))=1); !Lingo中除了一些特殊的模块，其他的语句均为约束语句;
@for(var(j):@sum(var(i):x(i,j))=1);
end


model:
sets:
var1/1..3/:c,x;
var2/1,2/:b;
link(var2,var1):a;!定义集合,以及赋给集合不同的属性名，有点像C语言里面的类class;
endsets

data:
a=1 1 1
  4 2 1;!给有属性名的集合赋值;
b=7 12;
c=-3 -2 -1;
enddata

min=@sum(var1:c*x);!目标函数，Lingo中识别目标函数是用max和min来，所以目标函数语句写在哪都可;
@bin(x(3));
@sum(var1(j):a(1,j)*x)<=b(1); !Lingo中除了一些特殊的模块，其他的语句均为约束语句;
@sum(var1(j):a(2,j)*x)=b(2);
end
