f=[3;2;1];
%aeq=[1,1,1];
a=[1,1,1;1,0,-1;0,1,-1];
b=[6;-4;-3];
[x,y]=linprog(f,a,b,[],[],zeros(3,1));