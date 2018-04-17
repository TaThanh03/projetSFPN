import numpy as np
import matplotlib.pyplot as plt
import time
def proj_corr(A,epss,K,tol) :
    
    
    start = time.time()
    vp = np.linalg.eigvals(A);
    taille = np.size(vp);
    
    zx = [[] for i in range(taille)]
    zy = [[] for i in range(taille)]
    
    for i in range(taille):
        #STEP 0: Compute the first point z1
        z1_old = 0;
        n, l = np.shape(A);
        theta0 = epss;
        d0 = 1j;
        lamb0 = vp[i];
        z = lamb0 + theta0*d0;
        u,g,v = np.linalg.svd(z*np.eye(n)-A);
        g = g[-1]
        k = 0;
        u_min = [];
        v_min = [];
        while(abs(g-epss)/epss>tol):
            z1_old = z;
            u,s,v = np.linalg.svd(z1_old*np.eye(n)-A);
            s =s[-1];
            u= u.T
            u_min = u[-1]
            v_min = v[-1]
            v_min = np.conj(v_min)
            z = z - ((s - epss)/(np.conj(d0)*(np.vdot(v_min,u_min))).real)*d0
            g = np.linalg.svd(z*np.eye(n)-A,compute_uv = 0);
            g = g[-1]
        z1 = z 
        #END STEP 0
        while(k<K):
            #STEP 1: Prediction
            tho = np.min(0.1,(0.5)*abs(z - vp[i]))
            r = 1j*(np.vdot(np.conj(v_min),u_min))/abs(np.vdot(v_min,u_min))
            z = z+tho*r
            #STEP 2: Correction
            u,s,v = np.linalg.svd(z*np.eye(n)-A)
            s = s[-1]
            u= u.T
            u_min = u[-1]
            v_min = v[-1]
            v_min = np.conj(v_min)
            z = z - ((s - epss)/(np.vdot(u_min,v_min)))
            zx[i].append(z.real);
            zy[i].append(z.imag);
            if(abs(z-z1) < 0.001*abs(z1)):
                break;
            k = k+1;
        
    for i in range(taille):
        plt.plot(zx[i],zy[i]);
    plt.show()
    end = time.time()
    mytime = end -start
    return taille, zx, zy, mytime


A = np.array([[1, 1, 1, 1],[2, 60, 2, 2],[1, 1, 20, 1],[1, 2, 5, 20*1j]])
proj_corr(A,0.3,100,0.0001)
