from compute_analytical import compute_psi
from plot_analytical import plot

# --- SAFE INPUT FUNCTION ---
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input: please enter an integer.")



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
    try:
        # Step 1: compute everything
        data = compute_psi()

        if data is None:
            print("Computation failed. Exiting program.")
            return

        # Step 2: choose which n to plot (SAFE LOOP)
        while True:
            chosen_n = get_int("Enter which n to plot: ")

            try:
                # Step 3: plot from computed data
                plot(data, chosen_n)
                break  # exit loop if successful

            except ValueError as e:
                print(f"Plot error: {e}")
                print("Please enter a valid n value from the dataset.")

    except Exception as e:
        print(f"Unexpected error in main_v1: {e}")



if __name__ == "__main__":
    main()