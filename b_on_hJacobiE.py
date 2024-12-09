from vpython import *
from scipy.special import ellipj  # For Jacobi elliptic functions
import numpy as np
import matplotlib.pyplot as plt


# Parameters
R = 0.3
wire = ring(pos=vector(0, 0, 0), axis=vector(0, 0, 1), radius=R, thickness=0.005)

g = 9.8
A =  70*pi/180  
w =  2 #Angular velocity of hoop (rad/s)
modulus = .99999   # Elliptic modulus (0 <= k <= 1)
###by increasing the elliptic modulous k we can see how the motion of the bead becomes non-linear###
###When the elliptic modulous is 1 the bead will remain at the same height due to the gravity and centrifugal forces equalling each other### 
t = 8
dt = 0.01

# Initial bead position
u = w * t
sn, cn, dn, _ = ellipj(u, modulus)
theta = A * sn
y = -R * cos(theta)
x = R * sin(theta) * cos(w * t)
z = R * sin(theta) * sin(w * t)
bead = sphere(pos=vector(x, y, z), radius=0.01, color=color.yellow, make_trail=True)

# Arrays to store data for graphing
time_data = []
theta_data = []

while t < 20:
    rate(100)
    
    # Update Jacobi elliptic function
    u = w * t
    sn, cn, dn, _ = ellipj(u, modulus)  # Calculate Jacobi elliptic functions
    theta = A * sn                      # Angular position follows Jacobi elliptic motion
    
    # Update hoop's axis for rotation
    wire.axis = vector(sin(w * t), 0, -cos(w * t))
    
    # Update bead position
    y = -R * cos(theta)
    x = R * sin(theta) * cos(w * t)
    z = R * sin(theta) * sin(w * t)
    bead.pos = vector(x, y, z)
    
    # Store data for plotting
    time_data.append(t)
    theta_data.append(theta)
    
    t += dt
    
    
# Plot the motion of the bead
plt.figure(figsize=(10, 6))
plt.plot(time_data, theta_data, label=f"Elliptic modulus k = {modulus}")
plt.title("Motion of the Bead on the Hoop")
plt.xlabel("Time (s)")
plt.ylabel("Angular Position (θ in radians)")
plt.grid(True)
plt.legend()
plt.show()