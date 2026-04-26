from src.stage5_comparison.main_v5 import run_comparison


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


def get_positive_int(prompt):
    while True:
        value = get_int(prompt)
        if value <= 0:
            print("Value must be greater than 0.")
        else:
            return value


def get_positive_float(prompt):
    while True:
        value = get_float(prompt)
        if value <= 0:
            print("Value must be greater than 0.")
        else:
            return value


def main():
    print("=== Quantum Solver ===\n")

    # --- INPUT ---
    n_start = get_int("Enter starting n: ")
    n_end = get_int("Enter ending n: ")

    while n_start > n_end:
        print("n_start must be <= n_end")
        n_start = get_int("Enter starting n: ")
        n_end = get_int("Enter ending n: ")

    n_step = get_positive_int("Enter step for n: ")
    L = get_positive_float("Enter well length L: ")
    h = get_positive_float("Enter step size h: ")
    num_steps = get_positive_int("Enter number of steps: ")
    z0 = get_float("Enter z0: ")
    psi0 = get_float("Enter psi0: ")

    params = {
        "n_start": n_start,
        "n_end": n_end,
        "n_step": n_step,
        "L": L,
        "h": h,
        "num_steps": num_steps,
        "z0": z0,
        "psi0": psi0
    }

    # --- RUN ---
    results = run_comparison(params)

    if results is None:
        print("\n❌ Computation failed.")
        return

    print("\n=== Comparison Results ===")

    for n, methods in results.items():
        print(f"\n{n}:")
        for method, stats in methods.items():
            print(f"  {method}:")
            print(f"    Std Dev: {stats['std']:.6f}")
            print(f"    Std Error: {stats['stderr']:.6f}")

    print("\n=== Done ===")


if __name__ == "__main__":
    main()