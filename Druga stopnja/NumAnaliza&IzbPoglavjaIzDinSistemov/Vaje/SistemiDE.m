% Počistimo jedro in spremenljivke
clear
clc

% Definiramo sisteme
syms x y;
% Sistem a)
xd = exp(x+y) - y;
yd = x*y - x;
% Sistem b)
%xd = x^2 - y^2;
%yd = x*y - 1;
% Sistem c)
%xd = x - y;
%yd = y - x;
% Sistem d)
%xd = x + 2*y;
%yd = 0;
% Sistem e)
%xd = x*(1 - x^2 - y^2) - y;
%yd = x + y*(1 - x^2 - y^2);

% Fiksne točke:

[x0, y0] = solve([xd == 0, yd == 0], [x, y], "Real", true);
% Jacobijeva matrika:

J = jacobian([xd; yd], [x; y]);

% Izpišemo Jacobijeve matrike v fiksnih točkah
for i=1:length(x0)
    fprintf('\nFiksna točka %d: (%.5f, %.5f)\n', i, double(x0(i)), double(y0(i)));
    J_ft = double(subs(J, [x, y],[x0(i), y0(i)])); % Poračuna Jacobijevo matriko v i-ti fiksni točki
    disp('Jacobijeva matrika v fiksni točki');
    disp(J_ft);
    disp('Lastni vrednosti');
    disp(eig(J_ft)); %eig(A) vrne seznam lastnih vrednosti matrike A
end

% Fazni portret:
[xg, yg] = meshgrid(-6.:0.5:6., -6.:0.5:6.); %Določimo mrežo (koordinatni sistem)
% Definiramo numerično različico sistema
dx = exp(xg + yg) - yg;
dy = xg .* yg - xg;

%Normiramo vektorje
D = sqrt(dx.^2 + dy.^2);
dxn = dx ./ D;
dyn = dy ./ D;

%Risanje faznega portreta:
figure;
quiver(xg, yg, dxn, dyn, 0.6, 'k', 'LineWidth', 0.8); %quiver(x, y, u, v, l, b) točki (x, y) določi puščico dolžine l in barve b s smerjo (u, v) in to
%nariše.
hold on;
plot(double(x0), double(y0), 'ro', 'MarkerSize', 5, 'LineWidth', 0.8); % 'ro' pomeni, da bo točka označena na grafu s krogcem.
xlabel('x');
ylabel('y');
title('Fazni portret sistema');