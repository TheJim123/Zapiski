% Numerične metode za reševanje nelinearnih enačb.

clc
clear
syms x
g1(x)= (x^3+1)/5;
x0=0.1;
nat1=1e-8;
format long;
[xp, tabPr, stKor]=navadnaIteracija(g1,x0,nat1,20)


g2(x)=x^3+x-1;
x02=0;
nat2=1e-15;

[xp2,tabPr2,stKor2] = tangentnaP(g2,x02,nat2,20)

