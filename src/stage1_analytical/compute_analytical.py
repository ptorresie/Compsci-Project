import numpy as np
import pandas as pd

def compute_psi(L=None, dx=None, n_values=None):
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
    if L is None:
        L = float(input("Enter the well length L: "))
    if dx is None:
        dx = float(input("Enter the step size dx: "))
    if n_values is None:
        n_start = int(input("Enter starting n: "))
        n_end = int(input("Enter ending n: "))
        n_step = int(input("Enter step for n: "))
        n_values = np.arange(n_start, n_end + 1, n_step)

    x_values = np.arange(0, L + dx, dx)

    # Vectorized computation of ψ(x)
    psi_values = np.sqrt(2 / L) * np.sin(
        (n_values[:, None] * np.pi * x_values[None, :]) / L
    )

    # Construct DataFrame
    df = pd.DataFrame(psi_values.T, columns=[f"n={n}" for n in n_values])
    df.insert(0, "x", x_values)

    return df


if __name__ == "__main__":
    data = compute_psi()
    print(data)