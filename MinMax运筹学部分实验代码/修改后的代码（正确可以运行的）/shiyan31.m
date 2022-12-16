%matlab:
f=[1,1];
intcon=[1;2];
A=[2,5;6,5;-1,0;0,-1];
b=[16;30;0;0];
[x,y]=intlinprog(-f,intcon,A,b);