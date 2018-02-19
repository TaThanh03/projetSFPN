function [centre,rayons] = disque2(A,eps)
[n, r] = size(A);
rayons = zeros(1,n);
for i = 1:n
    centre(i) = A(i,i);
    for j = 1:n
        if(i~=j)
            rayons(i) = rayons(i)+abs(A(i,j))+eps; %abs pour le module
        end
    end
end
end




