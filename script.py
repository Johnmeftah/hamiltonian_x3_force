import numpy as np
import matplotlib.pyplot as plt

# parameters
m = 1
k = 1
E = 1

x_max = (4 * E / k)**0.25
x_vals = np.linspace(-x_max, x_max, 1000)
p_vals = np.sqrt(2 * m * (E - 0.25 * k * x_vals**4))

plt.figure(figsize=(6, 4))
plt.plot(x_vals, p_vals, label=r"$+p$", color="orange")
plt.plot(x_vals, -p_vals, label=r"$-p$", color="orangered")
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.xlabel("$x$")
plt.ylabel("$p$")
plt.title("Phase-Space Orbit for $F_x = -kx^3$")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("phase_space_orbit.png", dpi=300)
plt.show()
