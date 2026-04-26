from compute_euler_improved import compute_euler_improved
from plot_euler_improved import plot

# --- SAFE INPUT FUNCTION ---
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input: please enter an integer.")


def main():
    try:
        # Step 1: compute data
        data = compute_euler_improved()

        if data is None:
            print("Computation failed. Exiting program.")
            return

        # Optional: print data (only if needed)
        print(data)

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
        print(f"Unexpected error in main_v3: {e}")

if __name__ == "__main__":
    main()