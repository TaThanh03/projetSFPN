function [max_r,min_r,max_i,min_i] = petits_rectangles(A,eps)
[centre,rayons] = disque2(A,eps)
[r, n] = size(centre)
max_r = zeros(1,n)
min_r = zeros(1,n)
max_i = zeros(1,n)
min_i = zeros(1,n)
for i = 1:n
    tmp1 = real(centre(i))+rayons(i)
    tmp2 = real(centre(i))-rayons(i)
    tmp3 = imag(centre(i))+rayons(i)
    tmp4 = imag(centre(i))-rayons(i)
    max_r(i) = tmp1
    min_r(i) = tmp2
    max_i(i) = tmp3
    min_i(i) = tmp4
    
end
end
    
