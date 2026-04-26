import numpy as np
import pandas as pd

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

def compute_euler_improved(data=None):
    """
    Compute ψ(x) using the Improved Euler (Heun) method.

    This method improves upon the standard Euler method by using
    a predictor-corrector approach, reducing truncation error
    and improving stability.

    Parameters
    ----------
    data : dict, optional
        Same structure as compute_euler input

    Returns
    -------
    pandas.DataFrame or None
        Computed ψ(x) values for each n

    Notes
    -----
    Provides better accuracy than Euler while maintaining
    relatively low computational cost.
    """
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

        for i in range(num_steps - 1):
            k1_psi = z[:, i]
            k1_z = -(k_values**2) * psi[:, i]

            U_psi = psi[:, i] + h * k1_psi
            U_z = z[:, i] + h * k1_z

            k2_psi = U_z
            k2_z = -(k_values**2) * U_psi

            psi[:, i + 1] = psi[:, i] + (h / 2) * (k1_psi + k2_psi)
            z[:, i + 1] = z[:, i] + (h / 2) * (k1_z + k2_z)

        # --- NUMERICAL SAFETY ---
        if not np.all(np.isfinite(psi)):
            print("Error: computation produced invalid values (NaN or inf)")
            return None

        # --- DATAFRAME ---
        df = pd.DataFrame(psi.T, columns=[f"n={n}" for n in n_values])
        df.insert(0, "x", x_vals)

        return df

    except Exception as e:
        print(f"Unexpected error in compute_euler_improved: {e}")
        return None


if __name__ == "__main__":
    data = compute_euler_improved()
    if data is not None:
        print(data)