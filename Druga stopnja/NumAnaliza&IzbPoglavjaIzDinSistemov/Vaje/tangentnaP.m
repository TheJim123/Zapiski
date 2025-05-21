function [x,pribl,k] = tangentnaP(f,x0,nat,n)
% Ta funkcija izvede tangentno metodo.
% Vhodni podatki
% f...iteracijska funkcija
% x0...začetni približek
% nat...kolikšno natančnost želimo
% n...maksimalno število korakov iteracije
% Izhodni podatki
% x...zadnji izračunan približek
% pribl...vektor izračunanih približkov
% k...število dejansko izvedenih korakov

syms x;
odvod=diff(f,x);
g= x-f/odvod;
[x,pribl,k]=navadnaIteracija(g,x0,nat,n);

end










