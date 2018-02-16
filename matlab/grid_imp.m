A = [1 2; 1 -1];
epss = 10;
m = 100;
function gridimp(A,epss,m) %je declare ma fonction et entre()les parametres
    [n, r] = size(A) %j'affecte a n la taille de A pour pouvoir faire la matrice identite de la meme taille
    [min_x, max_x, min_y, max_y] = gershdisc(A);
    x = linspace(min_x, max_x, m); %je decoupe un tableau qui va de -nb a nb et m parties egales.
    y = linspace(min_y, max_y, m); %memechose
    for k = 1 : m
        for j = 1 : m %mes deux boucles for imbriquees
        a=min(svd((x(k)+y(j)*1i)*eye(n)-A)); %le calcul du min de la svd avec les fonctions matlab min et svd et eye(n) une mat identite de taille n
        sigmin(j,k) = a; 
        end
    end
    [C,h] = contour(x,y,sigmin, [epss epss]); %je trace les lignes de niveau 
    %contour(x,y,sigmin, [epss epss]);
end



