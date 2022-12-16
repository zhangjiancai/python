%第二题
s=[1,1,2,2,3,3,4,4,4,5,6,6];
t=[2,3,3,5,4,6,5,6,2,7,5,7];
w=[8,7,3,6,4,1,4,3,2,9,7,8];
G=digraph(s,t,w);
plot(G,'EdgeLabel',G.Edges.Weight,'Layout','layered');
mf = maxflow(G,1,7)