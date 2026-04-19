import numpy as np
import pandas as pd

def compute_euler_improved(data=None):
    if data is None:
        n_start = int(input("Enter starting n: "))
        n_end = int(input("Enter ending n: "))
        n_step = int(input("Enter step for n: "))
        h = float(input("Enter the step length h: "))
        num_steps = int(input("Enter the number of steps: "))
        L = float(input("Enter the well length L: "))
        z0 = float(input("Enter the initial value z_0: "))
        psi0 = float(input("Enter the initial value psi_0: "))
    else:
        n_start = data["n_start"]
        n_end = data["n_end"]
        n_step = data["n_step"]
        h = data["h"]
        num_steps = data["num_steps"]
        L = data["L"]
        z0 = data["z0"]
        psi0 = data["psi0"]

    n_values = np.arange(n_start, n_end + 1, n_step)
    x_vals = np.arange(0, num_steps * h, h)
    k_values = n_values * np.pi / L

    psi = np.zeros((len(n_values), num_steps))
    z = np.zeros((len(n_values), num_steps))

    psi[:, 0] = psi0
    z[:, 0] = z0

    for i in range(num_steps - 1):
        k1_psi = z[:, i]
        k1_z = -(k_values**2) * psi[:, i]

        U_psi = psi[:, i] + h * k1_psi
        U_z = z[:, i] + h * k1_z

        k2_psi = U_z
        k2_z = -(k_values**2) * U_psi

        psi[:, i + 1] = psi[:, i] + (h / 2) * (k1_psi + k2_psi)
        z[:, i + 1] = z[:, i] + (h / 2) * (k1_z + k2_z)

    df = pd.DataFrame(psi.T, columns=[f"n={n}" for n in n_values])
    df.insert(0, "x", x_vals)

    return df


if __name__ == "__main__":
    data = compute_euler_improved()
    print(data)