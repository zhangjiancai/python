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
