matlab:

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


lingo:
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