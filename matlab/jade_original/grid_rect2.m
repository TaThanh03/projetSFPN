function grid_rect2(A,epss,m)
[max_r,min_r,max_i,min_i] = rectangle2(A,eps)%je declare ma fonction et entre()les parametres
[n, r] = size(A) %j'affecte a n la taille de A pour pouvoir faire la matrice identite de la meme taille
x = linspace(min_r,max_r,m) %je decoupe un tableau qui va de -nb a nb et m parties egales.
y = linspace(min_i,max_i,m) %memechose
for k = 1:m, for j = 1:m %mes deux boucles for imbriquees
        a=min(svd((x(k)+y(j)*1i)*eye(n)-A)); %le calcul du min de la svd avec les fonctions matlab min et svd et eye(n) une mat identite de taille n
        sigmin1(j,k) = a;
    end
end
[C,h] = contour(x,y,sigmin1,[epss epss]) %je trace les lignes de niveau


end
