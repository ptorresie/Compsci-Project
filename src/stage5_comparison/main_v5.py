import numpy as np

from src.stage5_comparison.compare_methods import compare_methods

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
    
    # --- STATUS TRACKER ---
    status = {
        "Analytical": True,
        "Euler": True,
        "Euler Improved": True,
        "RK4": True,
        "Comparison": True
    }

    try:
        # --- USER INPUT (SAFE) ---
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

        n_values = np.arange(n_start, n_end + 1, n_step)

        # --- COMPUTE ---
        data_analytical = compute_psi(L=L, dx=h, n_values=n_values)
        if data_analytical is None:
            print("Analytical computation failed.")
            status["Analytical"] = False

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
        if data_euler is None:
            status["Euler"] = False

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
        if data_euler_improved is None:
            status["Euler Improved"] = False

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
        if data_rk4 is None:
            status["RK4"] = False

        # --- CHECK COMPUTATIONS ---
        if any(d is None for d in [data_analytical, data_euler, data_euler_improved, data_rk4]):
            print("One or more methods failed. Skipping comparison.")
            status["Comparison"] = False
        else:
            # --- COMPARE ---
            results = compare_methods(
                data_analytical,
                data_euler,
                data_euler_improved,
                data_rk4
            )

            if results is None or len(results) == 0:
                print("Comparison failed or returned no results.")
                status["Comparison"] = False
            else:
                # --- PRINT RESULTS ---
                print("\n=== Comparison Results ===")

                for n, methods in results.items():
                    print(f"\n{n}:")
                    for method, stats in methods.items():
                        print(f"  {method}:")
                        print(f"    Std Dev: {stats['std']:.6f}")
                        print(f"    Std Error: {stats['stderr']:.6f}")

        # --- FINAL SUMMARY ---
        print("\n=== Execution Summary ===")

        for method, ok in status.items():
            if ok:
                print(f"✔ {method}: OK")
            else:
                print(f"⚠ {method}: Failed or unstable")

    except Exception as e:
        print(f"Unexpected error in main_v5: {e}")


if __name__ == "__main__":
    main()