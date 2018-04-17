function grid_par_comp(A,epss,m,E)
[max_r,min_r,max_i,min_i] = rectangle2(A,eps);%je declare ma fonction et entre()les parametres
[n, r] = size(A); %j'affecte a n la taille de A pour pouvoir faire la matrice identite de la meme taille
x = linspace(min_r,max_r,m); %je decoupe un tableau qui va de -nb a nb et m parties egales.
y = linspace(min_i,max_i,m);
cpt= 0;%memechose
for k = 1:m, for j = 1:m %mes deux boucles for imbriquees
        X = abs(inv(A - ((x(k)+y(j)*1i)*eye(n))));
        Y = X*E;
        p(j,k) = max(eig(Y));
        cpt = cpt+1;
        
    end
end
cpt
[C,h] = contour(x,y,p,[epss epss]); %je trace les lignes de niveau 


end

%A = [1 1 1 1; 2 60 2 2; 1 1 20 1; 1 2 5 20j]
%E = eye(4)
%grid_par_comp(A,1,100,E)
