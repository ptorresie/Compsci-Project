from compute_rk4 import compute_rk4
from plot_rk4 import plot

# --- SAFE INPUT FUNCTION ---
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input: please enter an integer.")


def main():
    """
    Execute the RK4 pipeline.

    Steps:
    1. Compute ψ(x) using RK4
    2. Ask user for n
    3. Plot result
    """
    try:
        # Step 1: compute data
        data = compute_rk4()

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
        print(f"Unexpected error in main_v4: {e}")


if __name__ == "__main__":
    main()