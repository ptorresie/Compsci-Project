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

def compute_psi(L = None, dx = None, n_values = None):
    """
    Compute the wave function ψ(x) for a particle in a 1D infinite potential well.

    The wave function is defined as:
        ψ_n(x) = sqrt(2 / L) * sin(nπx / L)

    Parameters
    ----------
    L : float, optional
        Length of the potential well. If None, the user is prompted for input.
    dx : float, optional
        Step size for discretizing the spatial domain. If None, the user is prompted.
    n_values : array-like, optional
        Iterable of quantum numbers n for which ψ(x) is computed.
        If None, the user is prompted for a range (start, end, step).

    Returns
    -------
    pandas.DataFrame
        DataFrame where:
        - First column is 'x' (spatial coordinate)
        - Subsequent columns are wave function values labeled as 'n=<value>'

    Notes
    -----
    The computation is fully vectorized for efficiency:
    - x values are generated using numpy.arange
    - ψ values are computed using broadcasting over n and x

    Raises
    ------
    ValueError
        If invalid numeric inputs are provided by the user (via conversion).
    """
    # Ask for input if parameters are not provided
    try:
        # --- INPUT HANDLING ---
        if L is None:
            L = get_positive_float("Enter the well length L: ")

        if dx is None:
            dx = get_positive_float("Enter the step size dx: ")

        if n_values is None:
            n_start = get_int("Enter starting n: ")
            n_end = get_int("Enter ending n: ")

            while n_start > n_end:
                print("n_start must be <= n_end")
                n_start = get_int("Enter starting n: ")
                n_end = get_int("Enter ending n: ")

            n_step = get_positive_int("Enter step for n: ")

            n_values = np.arange(n_start, n_end + 1, n_step)

        # --- VALIDATION ---
        if len(n_values) == 0:
            print("Error: n_values cannot be empty")
            return None

        # --- COMPUTATION ---
        x_values = np.arange(0, L + dx, dx)

        if len(x_values) == 0:
            print("Error: x_values is empty")
            return None

        psi_values = np.sqrt(2 / L) * np.sin(
            (n_values[:, None] * np.pi * x_values[None, :]) / L
        )

        # --- NUMERICAL SAFETY ---
        if not np.all(np.isfinite(psi_values)):
            print("Error: computation produced invalid values (NaN or inf)")
            return None

        # --- DATAFRAME ---
        df = pd.DataFrame(psi_values.T, columns=[f"n={n}" for n in n_values])
        df.insert(0, "x", x_values)

        return df

    except Exception as e:
        print(f"Unexpected error in compute_psi: {e}")
        return None


if __name__ == "__main__":
    data = compute_psi()
    if data is not None:
        print(data)