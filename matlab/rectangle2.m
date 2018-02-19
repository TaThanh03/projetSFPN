function [max_r,min_r,max_i,min_i] = rectangle2(A,eps)
[centre,rayons] = disque2(A,eps);
max_r = 0;
min_r = 0;
max_i = 0;
min_i = 0;
for i = 1:size(centre)
    tmp1 = real(centre(i))+rayons(i);
    tmp2 = imag(centre(i))+rayons(i);
    if(tmp1 > max_r)
        max_r = tmp1;
    end
    if(tmp1 < min_r)
        min_r = tmp1;
    end
    if(tmp2 > max_i)
        max_i = tmp2;
    end
    if(tmp2 < min_i)
        min_i = tmp2;
    end
end
end