function grid_petits_rect(A,epss,m)

[max_r,min_r,max_i,min_i] = petits_rectangles(A,eps); %je declare ma fonction et entre()les parametres
[n, r] = size(A);%j'affecte a n la taille de A pour pouvoir faire la matrice identite de la meme taille
x = zeros(1,n*m);
y = zeros(1,n*m);
for l = 1:n
    tmp1 = linspace(min_r(l),max_r(l),m);
    tmp2 = linspace(min_i(l),max_i(l),m) ;%memechose
    for k = 1:m
        x((l-1)*m+k) = tmp1(k);
        y((l-1)*m+k) = tmp2(k);
    end
end
for l = 1:n, for k = 1:m, for j = 1:m %mes deux boucles for imbriquees
        a=min(svd((x((l-1)*m+k)+y((l-1)*m+j)*1i)*eye(n)-A)); %le calcul du min de la svd avec les fonctions matlab min et svd et eye(n) une mat identite de taille n
        sigmin2(j+(l-1)*m,k+(l-1)*m) = a; 
        end
    end
end
for i = 1:n
    tmp1 = x(1+(i-1)*m:i*m);
    tmp2 = y(1+(i-1)*m:i*m);
    tmp3 = sigmin2(1+(i-1)*m:i*m,1+(i-1)*m:i*m);
    [C,h] = contour(tmp1,tmp2,tmp3, [epss epss]);
    hold on;%je trace les lignes de niveau 
end
end