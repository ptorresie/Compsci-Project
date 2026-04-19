import numpy as np
import pandas as pd

def compute_rk4(data=None):
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

    def f_psi(z_val):
        return z_val

    def f_z(psi_val, k_val):
        return -(k_val**2) * psi_val

    for i in range(num_steps - 1):
        k1_psi = h * f_psi(z[:, i])
        k1_z = h * f_z(psi[:, i], k_values)

        k2_psi = h * f_psi(z[:, i] + 0.5 * k1_z)
        k2_z = h * f_z(psi[:, i] + 0.5 * k1_psi, k_values)

        k3_psi = h * f_psi(z[:, i] + 0.5 * k2_z)
        k3_z = h * f_z(psi[:, i] + 0.5 * k2_psi, k_values)

        k4_psi = h * f_psi(z[:, i] + k3_z)
        k4_z = h * f_z(psi[:, i] + k3_psi, k_values)

        psi[:, i + 1] = psi[:, i] + (1 / 6) * (k1_psi + 2 * k2_psi + 2 * k3_psi + k4_psi)
        z[:, i + 1] = z[:, i] + (1 / 6) * (k1_z + 2 * k2_z + 2 * k3_z + k4_z)

    df = pd.DataFrame(psi.T, columns=[f"n={n}" for n in n_values])
    df.insert(0, "x", x_vals)

    return df


if __name__ == "__main__":
    data = compute_rk4()
    print(data)