import matplotlib.pyplot as plt

def plot(data, chosen_n):
     """
    Plot the Euler solution ψ(x) for a selected quantum number.

    Parameters
    ----------
    data : pandas.DataFrame
        Contains x values and ψ(x) for different n values

    chosen_n : int
        Quantum number to visualize

    Raises
    ------
    ValueError
        If the requested n is not present in the dataset

    Returns
    -------
    None
        Displays the plot
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
    plt.title(f"Euler solution for n = {chosen_n}")
    plt.grid(True)
    plt.show()