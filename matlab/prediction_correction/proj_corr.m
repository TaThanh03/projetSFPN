function proj_corr(A,epss,lamb0,K,tol,tho)
    vp = eig(A);
    taille = size(vp);
    taille = taille(1);
    i=0;
    z1_old = 0;
    [n, l] = size(A);
    theta0 = epss;
    d0 = 1i;
    z = lamb0 + theta0*d0;
    g = min(svd(z*eye(n)-A));
    k = 0;
    u_min = [];
    v_min = [];
    while(abs(g-epss)/epss>tol)
        z1_old = z;
        [u,s,v] = svd(z1_old*eye(n)-A);
        s = diag(s);
        [s,i] = min(s);
        u_min = u(1:n,i:i);
        v_min = v(1:n,i:i);
        z = z - ((s - epss)/real(conj(d0)*ctranspose(v_min)*u_min))*d0;
        g = min(svd(z*eye(n)-A));
    end
    z1 = z
    while(k<K)
        r = 1i*(transpose(v_min)*u_min)/abs(ctranspose(v_min)*u_min);
        z = z+tho*r;
        k = k+1;
        [u,s,v] = svd(z*eye(n)-A);
        s = diag(s);
        [s,i] = min(s);
        u_min = u(1:n,i:i);
        v_min = v(1:n,i:i);
        z = z - ((s - epss)/(ctranspose(u_min)*v_min))
        zx(k) = real(z);
        zy(k) = imag(z);
        real(z1)
        if(abs(z-z1) < 0.001*abs(z1))
            break;
        end
    end
    plot(zx,zy);
end