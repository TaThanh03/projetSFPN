function [max_r,min_r,max_i,min_i] = petits_rect(A,eps)
[centre,rayons] = disque2(A,eps);
[n,r] = size(A);
centre2 = [];
rayons2 = [];
tmp2 = [];
max_r = [];
min_r = [];
max_i = [];
min_i = [];
liste = zeros(n,n);
tmp = zeros(n,n);
for i = 1:n
    for j = (i+1):n
        dist = sqrt(((real(centre(i))-real(centre(j)))^2)+(imag(centre(i))-imag(centre(j))^2))  
        r = rayons(i)+rayons(j)
        if(dist<r)
            liste(i,j) = 1;
            liste(j,i) = 1;
        end
    end
end

while (isequal(tmp,liste)==0)
    tmp = liste;
    for i = 1:n
        for j = 1:n
            if(liste(i,j)==1)
                for k = 1:n
                    if(liste(i,k) == 1&& k~=j)
                        liste(j,k) = 1;
                    end
                    if(liste(k,j) == 1 && k~=i)
                        liste(k,i) = 1;
                    end
                end
            end
        end
    end
end

for i = 1:n
    liste(i,i) = 1;
end
i=1
while(i<=n)
    if(any(i==tmp2))
        i=i+1;
    else
        for j = 1:n
            if(liste(i,j)==1)
                centre2 = [centre2,centre(i)];
                centre2 = [centre2,centre(j)]
                rayons2 = [rayons2,rayons(i)];
                rayons2 = [rayons2,rayons(j)]
                tmp2 = [tmp2,j];
            end
        end
        i = i+1;
        [maxre,minre,maxim,minim] = rect(centre2,rayons2)
        pos = [minre,minim,maxre-minre,maxim-minim];
        rectangle('Position',pos);
        max_r = [max_r,maxre];
        min_r = [min_r,minre];
        max_i = [max_i,maxim];
        min_i = [min_i,minim];
        centre2 = []
        rayons2 = []
    end
end
end
           
            

