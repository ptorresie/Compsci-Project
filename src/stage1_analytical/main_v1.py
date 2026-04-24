from compute_analytical import compute_psi
from plot_analytical import plot

def main():
    """
    Main execution function for computing and plotting quantum wave functions.

    Workflow
    --------
    1. Computes wave function data using `compute_psi`.
    2. Prompts the user to input a quantum number n.
    3. Plots the corresponding wave function ψ(x) using the `plot` function.

    Raises
    ------
    ValueError
        If the user provides an invalid integer for n (propagated from int conversion
        or downstream validation in `plot`).

    Returns
    -------
    None
        Executes the workflow and displays the plot.
    """
    # Step 1: compute everything
    data = compute_psi()

    # Step 2: choose which n to plot
    chosen_n = int(input("Enter which n to plot: "))

    # Step 3: plot from computed data
    plot(data, chosen_n)


if __name__ == "__main__":
    main()