import numpy as np
import pandas as pd

def compute_euler(data=None):
    if data is None:
        n_start = int(input("Enter starting n: "))
        n_end = int(input("Enter ending n: "))
        n_step = int(input("Enter step for n: "))
        delta_x = float(input("Enter the step length Δx: "))
        num_steps = int(input("Enter the number of steps: "))
        L = float(input("Enter the well length L: "))
        z_0 = float(input("Enter the initial value z_0: "))
        psi_0 = float(input("Enter the initial value psi_0: "))
    else:
        n_start = data["n_start"]
        n_end = data["n_end"]
        n_step = data["n_step"]
        delta_x = data["delta_x"]
        num_steps = data["num_steps"]
        L = data["L"]
        z_0 = data["z_0"]
        psi_0 = data["psi_0"]

    n_values = np.arange(n_start, n_end + 1, n_step)
    x_values = np.arange(0, num_steps * delta_x, delta_x)
    k_values = n_values * np.pi / L

    psi = np.zeros((len(n_values), num_steps))
    z = np.zeros((len(n_values), num_steps))

    psi[:, 0] = psi_0
    z[:, 0] = z_0

    for i in range(num_steps - 1):
        z[:, i + 1] = z[:, i] - (k_values**2) * psi[:, i] * delta_x
        psi[:, i + 1] = psi[:, i] + z[:, i] * delta_x

    df = pd.DataFrame(psi.T, columns=[f"n={n}" for n in n_values])
    df.insert(0, "x", x_values)

    return df


if __name__ == "__main__":
    data = compute_euler()
    print(data)