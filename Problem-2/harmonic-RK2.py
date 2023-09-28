Task 1

import numpy as np
import matplotlib.pyplot as plt

# Initialize the physical properties of the system
dt=0.01
k=1.0   #spring constant in SI units
xeq=0.0 #equilibrium position of the particle on a spring
mass=0.1 # in kg
omega = np.sqrt(k/mass)
period = 2* np.pi/omega 

t_total = period * 5  #we simulate for a total of 5 periods
t_range = np.arange(0,t_total, dt) 


# The following is the function responsible to compute the elastic force
def felastic(k,xeq,x):
    force = - k * (x - xeq)
    return force

# Advance time using Euler's rule
def move_Euler(xpos,xvel):
    xacc = felastic(k, xeq, xpos) / mass
    xpos = xpos + xvel * dt
    xvel = xvel + xacc * dt

    return xpos,xvel


# Advance time using the Runge-Kutta rule at 2nd order
def move_RK2(xpos,xvel): 
    #It's easier to start from the bottom and work your way up
    # at time t
    xacc = #evaluate instantaeously using xpos 
    
    # at time t+dt/2
    xpos_half = xpos + # propagate using xvel
    xacc_half = # evaluate instantaeously using xpos_half
    xvel_half = xvel + # propagate using xacc

    # at time t+dt
    xpos = xpos + # propagate using xvel_half
    xvel = xvel + # propagate using xacc_half
    
    return xpos,xvel


#Euler's method
xpos = 1
xvel = 0
xEuler=[]

for t in t_range:
    force = felastic(k,xeq,xpos)
    xpos,xvel = move_Euler(xpos,xvel)
    xEuler.append(xpos)

#RK2 method to be completed here
#Initialize positions and velocities first
#Then integrate the equations of motion using move_RK2() 


#analytical result
xa =  [np.cos(omega*t) for t in t_range]


fig, ax = plt.subplots(1)
ax.plot(t_range, xEuler , 'b.', label='Euler')
ax.axvline(8.8)

ax.plot(t_range, xa , 'r-', label='Analytical')

ax.legend()
ax.set_ylim(-2,2)
ax.set_xlim(0,10)
ax.set_xlabel('time (s)')
ax.set_ylabel('x position (m)')


plt.title('Harmonic Motion: Numerical vs Analytic Solution')
plt.show()
