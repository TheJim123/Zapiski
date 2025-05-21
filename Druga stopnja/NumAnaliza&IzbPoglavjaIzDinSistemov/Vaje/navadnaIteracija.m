function [x,pribl,k] = navadnaIteracija(g,x0,nat,n)
% Funkcija za numerično metodo navadna iteracija.
% VHODNI PODATKI
% g...iteracijska funkcija
% x0...začetni približek
% nat...kolikšno natančnost želimo
% n...maksimalno število korakov iteracije
% IZHODNI PODATKI
% x...zadnji izračunan približek
% pribl...vektor izračunanih približkov
% k...število dejansko izvedenih korakov

k=0;
pribl=x0;

while (k==0 || abs(pribl(end)-pribl(end-1))>=nat) && k<n % || je logični ali
    pribl(k+2)=g(pribl(k+1));
    k=k+1;
end
x=pribl(end);
end









