import numpy as np

from src.stage5_comparison.compare_methods import compare_methods

from src.stage1_analytical.compute_analytical import compute_psi
from src.stage2_euler.compute_euler import compute_euler
from src.stage3_euler_improved.compute_euler_improved import compute_euler_improved
from src.stage4_rk4.compute_rk4 import compute_rk4


def main():
    # --- USER INPUT ---
    n_start = int(input("Enter starting n: "))
    n_end = int(input("Enter ending n: "))
    n_step = int(input("Enter step for n: "))
    L = float(input("Enter well length L: "))

    h = float(input("Enter step size h: "))
    num_steps = int(input("Enter number of steps: "))
    z0 = float(input("Enter z0: "))
    psi0 = float(input("Enter psi0: "))

    n_values = np.arange(n_start, n_end + 1, n_step)

    # --- COMPUTE ---
    data_analytical = compute_psi(L=L, dx=h, n_values=n_values)

    data_euler = compute_euler({
    "n_start": n_start,
    "n_end": n_end,
    "n_step": n_step,
    "delta_x": h,   # correct for Euler
    "num_steps": num_steps,
    "L": L,
    "z_0": z0,
    "psi_0": psi0,
})
    data_euler_improved = compute_euler_improved({
    "n_start": n_start,
    "n_end": n_end,
    "n_step": n_step,
    "h": h,   # MUST be "h"
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

    # --- COMPARE ---
    results = compare_methods(
        data_analytical,
        data_euler,
        data_euler_improved,
        data_rk4
    )

    # --- PRINT (MUST BE INSIDE main) ---
    print("\n=== Comparison Results ===")

    for n, methods in results.items():
        print(f"\n{n}:")
        for method, stats in methods.items():
            print(f"  {method}:")
            print(f"    Std Dev: {stats['std']:.6f}")
            print(f"    Std Error: {stats['stderr']:.6f}")


if __name__ == "__main__":
    main()