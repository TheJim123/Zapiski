% Naša prva Matlab datoteka.
clear
clc
close all

a=5;
b=3;
a+b

% Absolutna vrednost števila -4.
abs(-4);
% Zapis potenc z osnovo 10: aeb pomeni a*10^b
5e11;
% Izpis besedila "Izpisujem besedilo.".
disp("Izpisujem besedilo.")
% Matrike v Matlabu.
A = [1 2 3; 4 5 6; 7 8 9];
% Vektor s prvimi 6 naravnimi števili.
n=1:6;
%Vektor s sodimi števili od 20 do 40.
s=20:2:40;
% Matrika s samimi ničlami.
Z=zeros(3);
% Matrika s samimi enicami.
O=ones(3);
% Matrika 3x5 z naključnimi števili med 0 in 1.
R1 = rand(3, 5);
%Matrika 4x3 z naključnimi števili med 0 in 100.
R2=rand(4, 3)*100;
%Matrika 2x3 z naključnimi števili med 20 in 60.
R3=rand(2, 3)*40 + 20;
% Množenje matrik (operator *).
B=A*ones(3);
% Množenje med elementi matrik (operator .*) za matrike istih dimenzij.
C=B.*A;
% Kvadriranje matrike (operator ^).
D=C^2;
% Kvadriranje elementov matrike (operator .^).
P1=R1.^2;
% Seštevanje in množenje matrike s skalarjem.
a*A; %Skalarno množenje
a+A; %Prišteje a k vsaki komponenti od A
% Transponiranje matrike.
AT=transpose(A); %Krajše: AT = A'
% Inverz matrike.
R4=rand(3, 3)*80+20;
R4I=inv(R4); %Tudi: R4I = R4^(-1)
%Za sisteme linearnih enačb je bolj učinkovito: x = A\b kot pa x = inv(A)*b

% DOSTOP DO ELEMENTOV MATRIKE

% Dostop do elementa v 3 vrstici, 2 stolpcu.
A(3,2);
% Dostop do cele tretje kolone v matriki.
A(:, 3);
% Dostop do cele druge vrstice v matriki.
A(2, :);
% Izrez podmatrike iz originalne matrike: 
% od 2. do 3. vrstice, od 1. do 3. stolpca.
A(2:3, 1:3);
% Dostop do zadnjega elementa matrike.
A(end);
% Velikost matrike.
size(A);
% Maksimum v vsakem stolpcu
max(A);
% Maksimum celotne matrike
max(max(A)); % ali max(A, [], "all")
% Minimum v vsakem stolpcu
min(A);
% Minimum celotne matrike
min(min(A));
% Združevanje vektorjev v matriko.
v1=[1 5 7];
v2 = [3 1 -2];
V1 = [v1;v2];
V2 = [v1' v2'];