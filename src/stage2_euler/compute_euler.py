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

def compute_euler(data=None):
    """
    Compute the wave function ψ(x) using the Euler method.

    This function numerically solves the second-order Schrödinger equation
    by converting it into a system of first-order differential equations.
    The Euler method is used as a first-order approximation scheme.

    Parameters
    ----------
    data : dict, optional
        Dictionary containing input parameters:
        - n_start, n_end, n_step
        - delta_x (step size)
        - num_steps
        - L (well length)
        - z_0, psi_0 (initial conditions)

        If None, values are requested interactively.

    Returns
    -------
    pandas.DataFrame or None
        DataFrame containing:
        - x values
        - ψ(x) for each quantum number n

        Returns None if computation fails.

    Notes
    -----
    Euler method is simple but introduces significant numerical error,
    especially for oscillatory systems like quantum wave functions.
    """
    try:
        # --- INPUT HANDLING ---
        if data is None:
            n_start = get_positive_int("Enter starting n: ")
            n_end = get_positive_int("Enter ending n: ")
            n_step = get_positive_int("Enter step for n: ")
            delta_x = get_positive_float("Enter the step length Δx: ")
            num_steps = get_positive_int("Enter the number of steps: ")
            L = get_positive_float("Enter the well length L: ")
            z_0 = get_float("Enter the initial value z_0: ")
            psi_0 = get_float("Enter the initial value psi_0: ")
        else:
            n_start = data["n_start"]
            n_end = data["n_end"]
            n_step = data["n_step"]
            delta_x = data["delta_x"]
            num_steps = data["num_steps"]
            L = data["L"]
            z_0 = data["z_0"]
            psi_0 = data["psi_0"]

        # --- VALIDATION ---
        if n_step <= 0:
            raise ValueError("n_step must be > 0")

        if n_start > n_end:
            raise ValueError("n_start must be <= n_end")

        if delta_x <= 0:
            raise ValueError("delta_x must be > 0")

        if num_steps <= 1:
            raise ValueError("num_steps must be > 1")

        if L <= 0:
            raise ValueError("L must be > 0")

        # --- COMPUTATION ---
        n_values = np.arange(n_start, n_end + 1, n_step)

        if len(n_values) == 0:
            raise ValueError("n_values is empty")

        x_values = np.arange(0, num_steps * delta_x, delta_x)

        if len(x_values) == 0:
            raise ValueError("x_values is empty")

        k_values = n_values * np.pi / L

        psi = np.zeros((len(n_values), num_steps))
        z = np.zeros((len(n_values), num_steps))

        psi[:, 0] = psi_0
        z[:, 0] = z_0

        for i in range(num_steps - 1):
            z[:, i + 1] = z[:, i] - (k_values**2) * psi[:, i] * delta_x
            psi[:, i + 1] = psi[:, i] + z[:, i] * delta_x

        # --- VALIDATE OUTPUT ---
        if not np.all(np.isfinite(psi)):
            raise ValueError("Euler computation produced invalid values (NaN or inf)")

        # --- DATAFRAME ---
        df = pd.DataFrame(psi.T, columns=[f"n={n}" for n in n_values])
        df.insert(0, "x", x_values)

        return df

    except Exception as e:
        print(f"Error in compute_euler: {e}")
        return None


if __name__ == "__main__":
    data = compute_euler()
    if data is not None:
        print(data)