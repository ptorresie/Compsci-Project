import numpy as np
import pandas as pd

# --- SAFE INPUT FUNCTIONS ---
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input: please enter an integer.")


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input: please enter a number.")


def get_positive_float(prompt):
    while True:
        value = get_float(prompt)
        if value <= 0:
            print("Value must be greater than 0.")
        else:
            return value


def get_positive_int(prompt):
    while True:
        value = get_int(prompt)
        if value <= 0:
            print("Value must be greater than 0.")
        else:
            return value

def compute_rk4(data=None):
    try:
        # --- INPUT HANDLING ---
        if data is None:
            n_start = get_int("Enter starting n: ")
            n_end = get_int("Enter ending n: ")

            while n_start > n_end:
                print("n_start must be <= n_end")
                n_start = get_int("Enter starting n: ")
                n_end = get_int("Enter ending n: ")

            n_step = get_positive_int("Enter step for n: ")
            h = get_positive_float("Enter the step length h: ")
            num_steps = get_positive_int("Enter the number of steps: ")
            L = get_positive_float("Enter the well length L: ")

            z0 = get_float("Enter the initial value z_0: ")
            psi0 = get_float("Enter the initial value psi_0: ")

        else:
            try:
                n_start = data["n_start"]
                n_end = data["n_end"]
                n_step = data["n_step"]
                h = data["h"]
                num_steps = data["num_steps"]
                L = data["L"]
                z0 = data["z0"]
                psi0 = data["psi0"]
            except KeyError as e:
                print(f"Missing key in data dictionary: {e}")
                return None

        # --- VALIDATION ---
        if n_step <= 0:
            print("Error: n_step must be > 0")
            return None

        if h <= 0:
            print("Error: h must be > 0")
            return None

        if num_steps <= 1:
            print("Error: num_steps must be > 1")
            return None

        if L <= 0:
            print("Error: L must be > 0")
            return None

        # --- COMPUTATION ---
        n_values = np.arange(n_start, n_end + 1, n_step)

        if len(n_values) == 0:
            print("Error: n_values is empty")
            return None

        x_vals = np.arange(0, num_steps * h, h)

        if len(x_vals) == 0:
            print("Error: x_vals is empty")
            return None

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

            psi[:, i + 1] = psi[:, i] + (1 / 6) * (
                k1_psi + 2 * k2_psi + 2 * k3_psi + k4_psi
            )
            z[:, i + 1] = z[:, i] + (1 / 6) * (
                k1_z + 2 * k2_z + 2 * k3_z + k4_z
            )

        # --- NUMERICAL SAFETY ---
        if not np.all(np.isfinite(psi)):
            print("Error: computation produced invalid values (NaN or inf)")
            return None

        # --- DATAFRAME ---
        df = pd.DataFrame(psi.T, columns=[f"n={n}" for n in n_values])
        df.insert(0, "x", x_vals)

        return df

    except Exception as e:
        print(f"Unexpected error in compute_rk4: {e}")
        return None


if __name__ == "__main__":
    data = compute_rk4()
    if data is not None:
        print(data)