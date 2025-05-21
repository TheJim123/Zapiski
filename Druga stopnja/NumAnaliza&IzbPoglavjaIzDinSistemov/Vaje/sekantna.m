function [x,pribl,k] = sekantna(f,x0,x1,nat,n)
% Ta funkcija izvede sekantno metodo.
% Vhodni podatki
% f...iteracijska funkcija
% x0...začetni približek
% x1...drugi začetni približek
% nat...kolikšno natančnost želimo
% n...maksimalno število korakov iteracije
% Izhodni podatki
% x...zadnji izračunan približek
% pribl...vektor izračunanih približkov
% k...število dejansko izvedenih korakov

pribl=[x0,x1];
k=1;
fxn1=f(x0);
while abs(pribl(k+1)-pribl(k))>=nat && k<n
    fxn=f(pribl(k+1));
    pribl(k+2)=pribl(k+1)-fxn*(pribl(k+1)-pribl(k))/(fxn-fxn1);
    k=k+1;
    fxn1=fxn;
end
k=k-1;
x=pribl(end);
end








