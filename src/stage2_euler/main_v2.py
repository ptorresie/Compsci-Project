from compute_euler import compute_euler
from plot_euler import plot

# --- SAFE INPUT FUNCTION ---
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input: please enter an integer.")


def main():
     """
    Execute the Euler method pipeline.

    Workflow:
    1. Computes ψ(x) using the Euler method
    2. Prompts user to select a quantum number n
    3. Plots the corresponding wave function

    This function serves as an interactive entry point
    for testing and visualizing the Euler approximation.
    """
    try:
        # Step 1: compute data
        data = compute_euler()

        if data is None:
            print("Computation failed. Exiting program.")
            return

        # Step 2: choose n safely
        while True:
            chosen_n = get_int("Enter which n to plot: ")

            try:
                # Step 3: plot
                plot(data, chosen_n)
                break  # exit loop if successful

            except ValueError as e:
                print(f"Plot error: {e}")
                print("Please enter a valid n value from the dataset.")

    except Exception as e:
        print(f"Unexpected error in main_v2: {e}")


if __name__ == "__main__":
    main()