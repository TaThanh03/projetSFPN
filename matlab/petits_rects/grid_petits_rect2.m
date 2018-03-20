function grid_petits_rect2(A,epss,m)

[max_r,min_r,max_i,min_i] = petits_rect(A,eps); %je declare ma fonction et entre()les parametres
[n, r] = size(A);
[v, s] = size(max_r);%j'affecte a n la taille de A pour pouvoir faire la matrice identite de la meme taille
x = zeros(1,s*m);
y = zeros(1,s*m);
for l = 1:s
    tmp1 = linspace(min_r(l),max_r(l),m);
    tmp2 = linspace(min_i(l),max_i(l),m) ;%memechose
    for k = 1:m
        x((l-1)*m+k) = tmp1(k);
        y((l-1)*m+k) = tmp2(k);
    end
end
for l = 1:s, for k = 1:m, for j = 1:m %mes deux boucles for imbriquees
        a=min(svd((x((l-1)*m+k)+y((l-1)*m+j)*1i)*eye(n)-A)); %le calcul du min de la svd avec les fonctions matlab min et svd et eye(n) une mat identite de taille n
        sigmin2(j+(l-1)*m,k+(l-1)*m) = a; 
        end
    end
end
for i = 1:s
    tmp1 = x(1+(i-1)*m:i*m);
    tmp2 = y(1+(i-1)*m:i*m);
    tmp3 = sigmin2(1+(i-1)*m:i*m,1+(i-1)*m:i*m);
    [C,h] = contour(tmp1,tmp2,tmp3, [epss epss]);
    hold on;%je trace les lignes de niveau 
end
end
%A = [1 2 3 4 5; 2 3 4 5 6; 5 6 4 3 7; 3 8 7 9 6; 1 2 3 6 7]
%A = [1 0 4444 -1 3467 444 1 5; -100 -3 1 900 4 5 1 2; 1578 8 -9 5787 1 4 9 4; -2 -57577 5 6 -1 3575 4 9; -2 3478 -444 3 -8 574 2 5; -6547 1 -5 2577 -7 5 556 7; -2 8 -488 -6 3 5789 7 9; 3778 4 6 778 -1 4 -3 87989]


