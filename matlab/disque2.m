function [centre,rayons] = disque2(A,eps)
[n, r] = size(A);
rayons = zeros(1,n);
for i = 1:n
    centre(i) = A(i,i);
    for j = 1:n
        if(i~=j)
            rayons(i) = rayons(i)+abs(A(i,j)); %abs pour le module
        end
    end
    theta = 0:0.01:2*pi;
    rayon = rayons(i);
    x = rayon*cos(theta)+real(centre(i));
    y = rayon*sin(theta)+imag(centre(i));
    plot(x,y)
    axis equal
    hold on;
    rayons(i) = rayons(i) + sqrt(n)*eps;
end
end




