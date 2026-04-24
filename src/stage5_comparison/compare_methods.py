import numpy as np


def compare_methods(data_analytical, data_euler, data_euler_improved, data_rk4):
    """
    Compare each numerical method against analytical solution.

    Computes:
    - Standard deviation of error
    - Standard error of error

    for selected n values: min, median, max
    """

    results = {}

    # --- Extract n columns ---
    n_columns_all = [col for col in data_analytical.columns if col != "x"]

    n_numbers = [int(col.split("=")[1]) for col in n_columns_all]
    n_numbers_sorted = sorted(n_numbers)

    # Select representative n values
    n_min = n_numbers_sorted[0]
    n_max = n_numbers_sorted[-1]
    n_median = n_numbers_sorted[len(n_numbers_sorted) // 2]

    selected_n = [n_min, n_median, n_max]
    n_columns = [f"n={n}" for n in selected_n]

    print("\nSelected n values:", selected_n)

    # --- Compute stats per method ---
    for col in n_columns:
        psi_analytical = data_analytical[col].values
        psi_euler = data_euler[col].values
        psi_euler_improved = data_euler_improved[col].values
        psi_rk4 = data_rk4[col].values

        min_len = min(
            len(psi_analytical),
            len(psi_euler),
            len(psi_euler_improved),
            len(psi_rk4)
        )

        psi_analytical = psi_analytical[:min_len]

        # --- Errors ---
        error_euler = psi_euler[:min_len] - psi_analytical
        error_euler_improved = psi_euler_improved[:min_len] - psi_analytical
        error_rk4 = psi_rk4[:min_len] - psi_analytical

        # --- Remove invalid values ---
        def clean(arr):
            return arr[np.isfinite(arr)]

        error_euler = clean(error_euler)
        error_euler_improved = clean(error_euler_improved)
        error_rk4 = clean(error_rk4)

        # --- Compute stats ---
        def compute_stats(error):
            std = np.std(error)
            stderr = std / np.sqrt(len(error))
            return std, stderr

        std_euler, stderr_euler = compute_stats(error_euler)
        std_euler_improved, stderr_euler_improved = compute_stats(error_euler_improved)
        std_rk4, stderr_rk4 = compute_stats(error_rk4)

        results[col] = {
            "Euler": {
                "std": std_euler,
                "stderr": stderr_euler
            },
            "Euler Improved": {
                "std": std_euler_improved,
                "stderr": stderr_euler_improved
            },
            "RK4": {
                "std": std_rk4,
                "stderr": stderr_rk4
            }
        }

    return results