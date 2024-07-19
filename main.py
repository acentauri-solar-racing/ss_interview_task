# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# Loading the data
current_dir = os.path.dirname(os.path.abspath(__file__))
route = pd.read_csv(os.path.join(current_dir, 'route.csv')).to_numpy()
cars = pd.read_csv(os.path.join(current_dir, 'cars.csv')).to_numpy()


car_times = []

for car in cars[:]:
    name,m,A_front,A_pv,f_s,c_d,c_r,E_bat,P_motor,eta_pv,eta_motor,eta_bat =car
    E_bat *= 3.6e6
    step_x = 3000.0
    k = 100
    dx = step_x/k
    print(name)
    v = 10.42
    t = 0
    E_kin = 1/2*m*v**2
    for (i, x, e) in route[:,:]:
        for _ in range(k):
            dt = dx/v
            t += dt
            F = 1.17*A_front*c_d*v**2+m*9.81*c_r
            E_kin -= F*dx
            E_bat += A_pv*eta_pv*eta_bat*700*dt*(1-f_s) 
            if (E_bat>=0.1*3.6e6):
                E_mot = E_bat/(3*3.6e6)*P_motor*eta_motor*1000
                E_bat -= E_mot
                E_kin += E_mot
            v = np.sqrt(2*E_kin/m)
    print(t)
    car_times += [t]

plt.bar(np.arange(14)+1,np.array(car_times)/3600)
plt.show()
plt.savefig('plot.jpg')