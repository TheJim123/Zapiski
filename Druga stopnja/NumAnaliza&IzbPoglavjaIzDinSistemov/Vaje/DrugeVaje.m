clear
clc
close all

% Definicija simbolične funkcije f(x)=5x^2+3x.
syms f(x);
f(x)=5*x^2 + 3*x;
% Izračunajmo vrednost za x=1.
f(1);
% Prvi odvod funkcije f.
odv=diff(f);
% Vrednost odvoda v x=3.
odv(3);
% Seštevek funkcije f in njenega odvoda.
sest=f+odv;
% Vrednost seštevka funkcije in njenega odvoda.
sest(3);
% Drugi odvod funkcije g=5*x^3+3*y^2 po spremenljivki y.
syms g(x, y);
g(x, y)= 5*x^3+3*y^2;
diff(g,y,2);
% Nedoločeni integral funkcije f.
int(f);
% Določeni integral funkcije f od 2 do 5.
int(f, 2, 5);
% Določeni integral funkcije 1/x^2 od 1 do neskončno.
Lambda = @(x) 1/x^2; % Implicitno podajanje funkcij
int(1/x^2, x, 1, inf);

% DEFINICIJA FUNKCIJE 
% V ločeni datoteki definirajte funkcijo 'krog', ki bo sprejela podatek o
% polmeru kroga, vrnila pa bo njegov obseg in ploščino.

% Pokličemo funkcijo, ki smo jo sami napisali.
[obseg, ploscina]=Krog(1);

% V tej datoteki definirajte funkcijo 'kvadrat', ki bo sprejela podatek o
% dolžini stranice kvadrata, vrnila pa bo njegov obseg in ploščino. 
% PAZI: Funkcije raje definiraj v posebej datoteki! Če že moreš klicat
% funkcijo v isti datoteki, kot si jo definiral, jo pokliči pred
% definicijo, sicer dobiš error!
[obsegK, ploscinaK]=Kvadrat(2); %Tukaj klicem skripto "Kvadrat" ki ima funkcijo "Kvadrat"

%Če želiš uporabiti skripto polno funkcij, jo lahko "importaš" preko "Import data" (Zavihek "Home")
% Lahko tudi uporabiš ukaz "import" na začetku datoteke