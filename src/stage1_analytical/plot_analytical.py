import matplotlib.pyplot as plt

def plot(data, chosen_n):
    """
    Plot the wave function ψ(x) for a given quantum number n.

    Parameters
    ----------
    data : pandas.DataFrame
        DataFrame containing the x values and corresponding wave function
        values for different quantum numbers. Must include a column named "x"
        and columns formatted as "n=<value>" (e.g., "n=1", "n=2", etc.).

    chosen_n : int
        Quantum number n specifying which wave function column to plot.
        The function will look for a column named f"n={chosen_n}".

    Raises
    ------
    ValueError
        If the specified column corresponding to the chosen quantum number
        is not found in the DataFrame.

    Returns
    -------
    None
        Displays a matplotlib plot of ψ(x) versus x.
    """
    column_name = f"n={chosen_n}"

    if column_name not in data.columns:
        raise ValueError(f"{column_name} not found in data")

    x_values = data["x"]
    psi_values = data[column_name]

    plt.figure(figsize=(10, 5))
    plt.plot(x_values, psi_values)
    plt.xlabel("x")
    plt.ylabel("ψ(x)")
    plt.title(f"Wave function for n = {chosen_n}")
    plt.grid(True)
    plt.show()