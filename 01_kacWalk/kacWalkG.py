import numpy as np
import matplotlib.pyplot as plt

def kac_walk_2d(a, c, T, steps=1000):
    """
    Simulate a 2D Kac walk with Poisson reversals.
    
    Parameters:
    - a: Poisson rate for direction reversals
    - c: Speed of the particle
    - T: Total time of simulation
    - steps: Number of time steps
    
    Returns:
    - x: Array of shape (steps, 2) containing 2D positions
    """
    t = np.linspace(0, T, steps)
    dt = T / (steps - 1)  # Time step size
    x = np.zeros((steps, 2))  # 2D position array
    v = np.array([c, 0], dtype=float)  # Initial velocity (speed c along x-axis)
    
    # Possible velocity directions: left, right, up, down
    directions = np.array([[c, 0], [-c, 0], [0, c], [0, -c]], dtype=float)
    
    for i in range(1, steps):
        x[i] = x[i-1] + v * dt  # Update position
        if np.random.poisson(a * dt):  # Poisson event for reversal
            # Choose a new velocity vector (treat directions as list of arrays)
            v = directions[np.random.choice(4)]  # Select one of the 4 directions
    
    return x

def brownian_2d(T, steps=100):
    t = np.linspace(0, T, steps)
    dt = T / (steps - 1)
    x = np.zeros((steps, 2))
    for i in range(1, steps):
        x[i] = x[i-1] + np.random.normal(0, np.sqrt(dt), 2)
    return x


# Example parameters from the paper (e.g., vizIdeas.md: a=4, c=2)
a, c, T = 4, 2, 100000
kpath = kac_walk_2d(a, c, T)
bpath = brownian_2d(T, T)

kFlag = True
if kFlag:
    plt.plot(kpath[:, 0], kpath[:, 1],
             label=f"Kac Walk (a={a}, c={c})")
    plt.title(f"2D Kac Walk (a={a}, c={c}, T={T})")
else:
    plt.plot(bpath[:, 0], bpath[:, 1],
             label=f"Brownian Motion")
    plt.title(f"2D Brownian Motion (T={T})")
    
plt.xlabel("X position")
plt.ylabel("Y position")

plt.legend()
plt.grid(True)
plt.show()

