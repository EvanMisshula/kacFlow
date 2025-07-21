import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def diffusion_velocity_norm(t, sigma=1):
    """Approximate L^2 norm of diffusion velocity field: ||v_t||^2 ~ 1/(1-t)."""
    return 1 / (1 - t + 1e-6)  # Avoid division by zero

def kac_velocity_norm(t, c=2, d=1):
    """L^2 norm of Kac velocity field: ||v_t||^2 <= d * c^2."""
    return d * c**2 * np.ones_like(t)  # Constant bound

def diffusion_velocity_field(x, t, sigma=1):
    """Diffusion velocity field (approximate score-based): v_t(x) ~ -x/(1-t)."""
    return -x / (1 - t + 1e-6)

def kac_velocity_field(x, t, a=4, c=2):
    """Simplified Kac velocity field (1D, approximate from paper's Corollary 15)."""
    # Placeholder: assume mean-reverting behavior toward target N(0,1)
    return -a * x  # Simplified linear velocity field

# Time points
t = np.linspace(0, 0.99, 100)  # Avoid t=1 for diffusion

# 🌟 Global font scaling (50% larger than original)
plt.rcParams.update({
    'font.size': 27,          # was 18
    'axes.titlesize': 30,     # was 20
    'axes.labelsize': 27,     # was 18
    'xtick.labelsize': 24,    # was 16
    'ytick.labelsize': 24,    # was 16
    'legend.fontsize': 24,    # was 16
    'figure.titlesize': 33,    # was 22
    'pdf.fonttype': 42,  # Embed fonts (TrueType)
    'ps.fonttype': 42,
})
# # GLOBAL FONT SETTINGS
# plt.rcParams.update({
#     'font.size': 18,
#     'axes.titlesize': 20,
#     'axes.labelsize': 18,
#     'xtick.labelsize': 16,
#     'ytick.labelsize': 16,
#     'legend.fontsize': 16,
#     'figure.titlesize': 22
# })


# Plot 1: L^2 norm comparison
plt.figure(figsize=(10, 5))
plt.plot(t, diffusion_velocity_norm(t), label=r"Diffusion $\|v_t\||^2$", color='red')
plt.plot(t, kac_velocity_norm(t, c=2, d=1), label=r"Kac $\|v_t\|^2$ (bound)", color='blue')
plt.xlabel(r"Time $t$")

plt.ylabel(r"$\|v_t\|^2$", 
rotation=0, labelpad=40, loc='center')  # Horizontal y-axis label
# plt.ylabel(r"$||v_t||^2$")
plt.title("Velocity Field Norm: Diffusion (Exploding) vs. Kac (Bounded)")
plt.legend()
plt.grid(True)
output_dir = "../graphics"

plt.savefig(os.path.join(output_dir, "02_1_velFieldNorm.pdf"), bbox_inches='tight')
plt.savefig(os.path.join(output_dir, "02_1_velFieldNorm_zoom.png"), bbox_inches='tight', dpi=220)

plt.show()

# Plot 2: Velocity field at specific times
x = np.linspace(-5, 5, 50)
times = [0.1, 0.5, 0.9]
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 8), constrained_layout=True)

for t in times:
    ax1.plot(x, diffusion_velocity_field(x, t), label=f"Diffusion, t={t}")
    ax2.plot(x, kac_velocity_field(x, t), label=f"Kac, t={t}")

ax1.set_xlabel(r"$x$")
# ax1.set_ylabel(r"$v_{t}(x)$",rotation=0, labelpad=40, loc='center')  # Horizontal y-axis label)
#ax1.set_ylabel(r"$v_{t}(x)$", rotation=0, labelpad=70, ha='right', va='center', loc='center')
ax1.set_ylabel(r"$v_{t}(x)$", rotation=0, labelpad=70, ha='right', va='center')
ax1.legend(loc='upper center', bbox_to_anchor=(0.5,-0.20), frameon=False)


ax1.set_title("Diffusion Velocity Field")
#ax1.legend()
ax1.grid(True)

ax2.set_xlabel(r"$x$")
#ax2.set_ylabel(r"$v_{t}(x)$",rotation=0, labelpad=40, loc='center')  # Horizontal y-axis label)
#ax2.set_ylabel(r"$v_{t}(x)$", rotation=0, labelpad=70, ha='right', va='center', loc='center')
ax2.set_ylabel(r"$v_{t}(x)$", rotation=0, labelpad=60, ha='right', va='center')
ax2.set_title("Kac Velocity Field")
#ax2.legend()
ax2.legend(loc='upper center', bbox_to_anchor=(0.5,-0.20), frameon=False)
ax2.grid(True)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, "02_2_velField.pdf"), bbox_inches='tight')
plt.savefig(os.path.join(output_dir, "02_2_velField_zoom.png"), bbox_inches='tight', dpi=220)


plt.show()


import plotly.graph_objects as go
from plotly.subplots import make_subplots

t = np.linspace(0, 0.99, 100)
fig = go.Figure()
fig.add_trace(go.Scatter(x=t, y=diffusion_velocity_norm(t), name="Diffusion ||v_t||^2", line=dict(color='red')))
fig.add_trace(go.Scatter(x=t, y=kac_velocity_norm(t, c=2, d=1), name="Kac ||v_t||^2", line=dict(color='blue')))
fig.update_layout(title="Velocity Field Norm: Diffusion vs. Kac", xaxis_title="Time t", yaxis_title="||v_t||^2")
fig.show()
