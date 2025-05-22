clear
clc
% Najprej dve realni lastni vrednosti
k1 = 2; % Koeficient k
o1 = 1; % Koeficient omega
% Nato dvojna realna lastna vrednost
k2=2;
o2=2;
% Na koncu še dve kompleksni lastni vrednosti
k3=1;
o3=2;
% Definiramo sisteme
sys1=@(t, x) [x(2); -o1^2*x(1) - 2*k1*x(2)]; % Sistem 1

sys2=@(t, x) [x(2); -o2^2*x(1) - 2*k2*x(2)]; % Sistem 2

sys3=@(t, x) [x(2); -o3^2*x(1) - 2*k3*x(2)]; % Sistem 3

warning off MATLAB:divideByZero;

% Pripravimo mrežo za fazne portrete
[xg, yg] = meshgrid(-5:.2:5, -5:.2:5);
% Numerična različica sistema
dx = yg;
dy1 = -o1^2.*xg - 2*k1.*yg;
dy2 = -o2^2.*xg - 2*k2.*yg;
dy3 = -o3^2.*xg - 2*k3.*yg;
% Vektorje normaliziramo
D1 = sqrt(dx.^2 + dy1.^2);
D2 = sqrt(dx.^2 + dy2.^2);
D3 = sqrt(dx.^2 + dy3.^2);
%
dxn1 = dx./D1;
dyn1 = dy1./D1;
%
dxn2 = dx./D2;
dyn2 = dy2./D2;
%
dxn3 = dx./D3;
dyn3 = dy3./D3;

% Najprej narišemo rešitve
% Prvi graf
figure;
hold on;
for x0=-3:3;
    for y0=-3:3;
        [ts1, xs1] = ode45(sys1, [0, 5], [x0, y0]);
        plot(ts1, xs1(:,1));
    end
end
xlabel('t');
ylabel('x(t)');
title('Graf rešitve x pri dveh realnih lastnih vrednostih');
saveas(gcf, 'Rešitev1.png');
% Drugi graf
figure;
hold on;
for x0=-3:3;
    for y0=-3:3;
        [ts2, xs2] = ode45(sys2, [0, 5], [x0, y0]);
        plot(ts2, xs2(:,1));
    end
end
xlabel('t');
ylabel('x(t)');
title('Graf rešitve x pri eni realni lastni vrednosti');
saveas(gcf, 'Rešitev2.png');
% Tretji graf
figure;
hold on;
for x0=-3:3;
    for y0=-3:3;
        [ts3, xs3] = ode45(sys3, [0, 5], [x0, y0]);
        plot(ts3, xs3(:,1));
    end
end
xlabel('t');
ylabel('x(t)');
title('Graf rešitve x pri dveh kompleksnih lastnih vrednostih');
saveas(gcf, 'Rešitev3.png');
% Fazni portreti

figure;

% Dve realni lastni vrednosti

quiver(xg, yg, dxn1, dyn1, 0.5, 'b', 'LineWidth', 0.7);
hold on;
plot(0, 0, 'ro', 'MarkerSize', 5, 'LineWidth', 0.7);
xlabel('x');
ylabel('y');
title('Fazni portret sistema z dvema realnima lastnima vrednostima');
saveas(gcf, 'Fazni1.png');
% Ena realna lastna vrednost

figure;
quiver(xg, yg, dxn2, dyn2, 0.5, 'b', 'LineWidth', 0.7);
hold on;
plot(0, 0, 'ro', 'MarkerSize', 5, 'LineWidth', 0.7);
xlabel('x');
ylabel('y');
title('Fazni portret sistema z eno realno lastno vrednostjo');
saveas(gcf, 'Fazni2.png');
% Dve kompleksni lastni vrednosti

figure;
quiver(xg, yg, dxn3, dyn3, 0.5, 'b', 'LineWidth', 0.7);
hold on;
plot(0, 0, 'ro', 'MarkerSize', 5, 'LineWidth', 0.7);
xlabel('x');
ylabel('y');
title('Fazni portret sistema z dvema kompleksnima lastnima vrednostima');
saveas(gcf, 'Fazni3.png');