function [max_r,min_r,max_i,min_i] = rect(centre,rayons)
[r, n] = size(centre);
max_r = real(centre(1))+rayons(1);
min_r = real(centre(1))-rayons(1);
max_i = imag(centre(1))+rayons(1);
min_i = imag(centre(1))-rayons(1);
for i = 2:n
    tmp1 = real(centre(i))+rayons(i);
    tmp2 = real(centre(i))-rayons(i);
    tmp3 = imag(centre(i))+rayons(i);
    tmp4 = imag(centre(i))-rayons(i);
    if(tmp1 > max_r)
        max_r = tmp1;
    end
    if(tmp2 < min_r)
        min_r = tmp2;
    end
    if(tmp3 > max_i)
        max_i = tmp3;
    end
    if(tmp4 < min_i)
        min_i = tmp4;
    end
end
end