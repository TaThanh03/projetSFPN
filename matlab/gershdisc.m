function [min_x, max_x, min_y, max_y] = gershdisc(A)
max_x = 0;
max_y = 0;
min_x = 0;
min_y = 0;
for i = 1:size(A,1)
    h = real(A(i,i)); 
    k = imag(A(i,i)); 
    r = 0;
    for j = 1:size(A,1)
        if i ~= j 
            r=r+(norm(A(i,j)));
        end
        if (h - r) < min_x
            min_x = (h - r);
        end
        if (h + r) > max_x
            max_x = (h + r);
        end
        if (k - r) < min_y
            min_y = (k - r);
        end
        if (k + r) > max_y
            max_y = (k + r);
        end
    end
end

end