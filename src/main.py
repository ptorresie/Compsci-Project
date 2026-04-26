import numpy as np
import matplotlib.pyplot as plt

from src.stage5_comparison.main_v5 import run_comparison

from src.stage1_analytical.compute_analytical import compute_psi
from src.stage2_euler.compute_euler import compute_euler
from src.stage3_euler_improved.compute_euler_improved import compute_euler_improved
from src.stage4_rk4.compute_rk4 import compute_rk4


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

    # --- RUN COMPARISON ---
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

    # =========================
    # 🔹 OPTIONAL PLOTTING
    # =========================

    plot_choice = input("\nDo you want to plot results? (y/n): ").lower()

    if plot_choice == "y":
        print(f"Available n values: {list(range(n_start, n_end + 1, n_step))}")
        n_plot = get_int("Enter n value to plot: ")

        # recompute all methods for plotting (clean separation)
        n_values = np.arange(n_start, n_end + 1, n_step)

        data_analytical = compute_psi(L=L, dx=h, n_values=n_values)

        data_euler = compute_euler({
            "n_start": n_start,
            "n_end": n_end,
            "n_step": n_step,
            "delta_x": h,
            "num_steps": num_steps,
            "L": L,
            "z_0": z0,
            "psi_0": psi0,
        })

        data_euler_improved = compute_euler_improved({
            "n_start": n_start,
            "n_end": n_end,
            "n_step": n_step,
            "h": h,
            "num_steps": num_steps,
            "L": L,
            "z0": z0,
            "psi0": psi0,
        })

        data_rk4 = compute_rk4({
            "n_start": n_start,
            "n_end": n_end,
            "n_step": n_step,
            "h": h,
            "num_steps": num_steps,
            "L": L,
            "z0": z0,
            "psi0": psi0,
        })

        # --- PLOT ---
        try:
            col = f"n={n_plot}"

            plt.figure(figsize=(10, 5))

            plt.plot(data_analytical["x"], data_analytical[col],label="Analytical", linestyle='-', linewidth=3, color='blue')

            plt.plot(data_euler["x"], data_euler[col],label="Euler", linestyle='--', marker='o', markevery=10, alpha=0.8)

            plt.plot(data_euler_improved["x"], data_euler_improved[col], label="Euler Improved", linestyle='-.', marker='s', markevery=10, alpha=0.8)

            plt.plot(data_rk4["x"], data_rk4[col], label="RK4", linestyle=':', marker='x', markevery=10, alpha=0.8)

            plt.xlabel("x")
            plt.ylabel("ψ(x)")
            plt.title(f"Comparison of methods for n = {n_plot}")
            plt.legend()
            plt.grid(True)
            plt.show()

        except KeyError:
            print(f"Invalid n value: n={n_plot} not found")

        except Exception as e:
            print(f"Plot error: {e}")


if __name__ == "__main__":
    main()