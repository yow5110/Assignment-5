# Week 6 Task 1

import numpy as np
import matplotlib.pyplot as plt

# Initialize the physical properties of the system
dt=0.01
k=1.0   #spring constant in SI units
xeq=0.0 #equilibrium position of the particle on a spring
mass=0.1 # in kg
omega = np.sqrt(k/mass)
period = 2* np.pi/omega 

t_total = period * 5 /dt  #we simulate for a total of 5 periods
t_range = range(int(t_total))
realtime_range = [it*dt for it in range(int(t_total)+1)] #to plot x against real time t later


# The following is the function responsible to compute the elastic force
def felastic(k,xeq,x):
    force = - k * (x - xeq)
    return force

# Advance time using Euler's rule
def move_Euler(dt,xpos,xvel):
    xacc = felastic(k, xeq, xpos) / mass
    xpos = xpos + xvel * dt
    xvel = xvel + xacc * dt

    return xpos,xvel

# Advance time using the Runge-Kutta rule at 2nd order
def move_RK2(dt,xpos,xvel): 
    #It's easier to start from the bottom and work your way up
    #1. at time t
    xacc = #evaluate instantaeously using xpos 
    
    #2. at time t+dt/2
    xpos_half = xpos + # propagate using xvel
    xacc_half = # evaluate instantaeously using xpos_half
    xvel_half = xvel + # propagate using xacc

    #3. at time t+dt
    xpos = xpos + # propagate using xvel_half
    xvel = xvel + # propagate using xacc_half
    
    return xpos,xvel

#Euler result
xpos = 1
xvel = 0
xEuler=[xpos]
for it in t_range:
    force = felastic(k,xeq,xpos)
    xpos,xvel = move_Euler(dt,xpos,xvel)
    xEuler.append(xpos)

#RK2 result 
xpos = 1
xvel = 0
xRK2=[xpos]
for it in t_range:
    force = felastic(k,xeq,xpos)
    xpos,xvel = move_RK2(dt,xpos,xvel)
    xRK2.append(xpos)

#analytical result
xa =  [np.cos(omega*t) for t in realtime_range]


fig, ax = plt.subplots(1)
ax.plot(realtime_range, xEuler , 'b.', label='Euler')
ax.plot(realtime_range, xRK2 , 'g.', label='RK2')
ax.axvline(8.8)

ax.plot(realtime_range, xa , 'r-', label='Analytical')

ax.legend()
ax.set_ylim(-2,2)
ax.set_xlim(0,10)
ax.set_xlabel('time (s)')
ax.set_ylabel('x position (m)')


plt.title('Harmonic Motion: Numerical vs Analytic Solution')
plt.show()