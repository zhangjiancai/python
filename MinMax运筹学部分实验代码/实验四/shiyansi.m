s=[1,1,2,2,3,3,4,4,5,6];
t=[2,3,5,4,4,6,5,6,7,7];
w=[20,15,24,8,10,6,10,8,11,20];
G=digraph(s,t,w);
plot(G,'EdgeLabel',G.Edges.Weight,'linewidth',2);
set(gca,'XTick',[],'YTick',[]);

[P,d] = shortestpath(G,1,7); %注意:该函数matlab2015b之后才有

%在图中高亮我们的最短路径
myplot = plot(G,'EdgeLabel',G.Edges.Weight,'linewidth',2); %首先将图赋给一个变量
highlight (myplot,P,'EdgeColor','r');%对这个变量即我们刚刚绘制的图形进行高亮处理

%第二题
s=[1,1,2,2,3,3,4,4,4,5,6,6];
t=[2,3,3,5,4,6,5,6,2,7,5,7];
w=[8,7,3,6,4,1,4,3,2,9,7,8];
G=digraph(s,t,w);
plot(G,'EdgeLabel',G.Edges.Weight,'Layout','layered');
mf = maxflow(G,1,7)