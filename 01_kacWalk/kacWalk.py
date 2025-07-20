import numpy as np
import matplotlib.pyplot as plt

def simulate_kac_walk_2d(a, c, T=5.0, dt=0.01, n_paths=5):
    """
    Simulate 2D Kac walks using a velocity-flipping process.
    
    Parameters:
        a (float): Poisson rate (direction flip frequency)
        c (float): constant speed magnitude
        T (float): total simulation time
        dt (float): time step
        n_paths (int): number of independent trajectories to simulate
    
    Returns:
        np.ndarray: shape (n_paths, n_steps, 2), simulated 2D paths
    """
    n_steps = int(T / dt)
    xpaths = np.zeros((n_paths, n_steps, 2))

    for path in range(n_paths):
        x = np.zeros(2)  # start at origin
        v = c * np.random.choice([-1, 1], size=2)  # random initial direction

        for t in range(n_steps):
            if np.random.rand() < a * dt:
                flip_axis = np.random.choice([0, 1])  # randomly flip x or y component
                v[flip_axis] *= -1
            x += v * dt
            xpaths[path, t] = x

    return xpaths

# --- Main script to plot multiple (a, c) settings ---
param_list = [(1, 1), (2, 1), (4, 2), (25, 5)]
colors = ['r', 'g', 'b', 'm']
T = 5.0
dt = 0.01
n_paths = 5

fig, axs = plt.subplots(2, 2, figsize=(12, 10))
axs = axs.flatten()

for i, (a, c) in enumerate(param_list):
    paths = simulate_kac_walk_2d(a, c, T=T, dt=dt, n_paths=n_paths)
    ax = axs[i]
    for p in range(n_paths):
        ax.plot(paths[p, :, 0], paths[p, :, 1], alpha=0.8)
    ax.set_title(f"Kac Walk: a={a}, c={c}")
    ax.set_xlim(-20, 20)
    ax.set_ylim(-20, 20)
    ax.set_aspect('equal')
    ax.grid(True)

plt.tight_layout()
plt.suptitle("2D Kac Walk Trajectories for Varying (a, c)", fontsize=16, y=1.02)
plt.show()
