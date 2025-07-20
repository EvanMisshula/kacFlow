import os
import numpy as np
import matplotlib.pyplot as plt

# GLOBAL FONT SETTINGS
plt.rcParams.update({
    'font.size': 18,
    'axes.titlesize': 20,
    'axes.labelsize': 18,
    'xtick.labelsize': 16,
    'ytick.labelsize': 16,
    'legend.fontsize': 16,
    'figure.titlesize': 22
})

def kac_walk_2d(a, c, T, steps=1000):
    t = np.linspace(0, T, steps)
    dt = T / (steps - 1)
    x = np.zeros((steps, 2))
    v = np.array([c, 0], dtype=float)
    directions = np.array([[c, 0], [-c, 0], [0, c], [0, -c]], dtype=float)
    for i in range(1, steps):
        x[i] = x[i-1] + v * dt
        if np.random.rand() < a * dt:
            v = directions[np.random.choice(4)]
    return x

def brownian_2d(T, steps=1000):
    dt = T / (steps - 1)
    x = np.zeros((steps, 2))
    for i in range(1, steps):
        x[i] = x[i-1] + np.random.normal(0, np.sqrt(dt), 2)
    return x

# Parameters
a, c, T = 4, 2, 10
steps = 2000
kpath = kac_walk_2d(a, c, T, steps)
bpath = brownian_2d(T, steps)

# Plot
fig, axs = plt.subplots(1, 2, figsize=(14, 6), dpi=220)

axs[0].plot(kpath[:, 0], kpath[:, 1], label=f"Kac Walk (a={a}, c={c})", color='blue')
axs[0].set_title("2D Kac Walk")
axs[0].set_xlabel("X")
axs[0].set_ylabel("Y")
axs[0].axis('equal')
axs[0].grid(True)
axs[0].legend()

axs[1].plot(bpath[:, 0], bpath[:, 1], label="Brownian Motion", color='orange')
axs[1].set_title("2D Brownian Motion")
axs[1].set_xlabel("X")
axs[1].set_ylabel("Y")
axs[1].axis('equal')
axs[1].grid(True)
axs[1].legend()

plt.suptitle("Kac Walk vs Brownian Motion", fontsize=22)
plt.tight_layout()
plt.subplots_adjust(top=0.88)
output_dir = "../graphics"

plt.savefig(os.path.join(output_dir, "kac_vs_bm.pdf"), bbox_inches='tight')
plt.savefig(os.path.join(output_dir, "kac_vs_bm_zoom.png"), bbox_inches='tight', dpi=220)


plt.show()

