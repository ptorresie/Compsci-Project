<<<<<<< HEAD
import numpy as np


def compare_methods(data_analytical, data_euler, data_euler_improved, data_rk4):
    """
    Compare each numerical method against analytical solution.

    Computes:
    - Standard deviation of error
    - Standard error of error

    for selected n values: min, median, max
    """

    try:
        # --- CHECK INPUT DATA ---
        if any(d is None for d in [data_analytical, data_euler, data_euler_improved, data_rk4]):
            print("Error: one or more input datasets are None")
            return None

        results = {}

        # --- Extract n columns ---
        n_columns_all = [col for col in data_analytical.columns if col != "x"]

        if len(n_columns_all) == 0:
            print("Error: no n columns found in analytical data")
            return None

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
            try:
                psi_analytical = data_analytical[col].values
                psi_euler = data_euler[col].values
                psi_euler_improved = data_euler_improved[col].values
                psi_rk4 = data_rk4[col].values
            except KeyError:
                print(f"Warning: column {col} not found in one dataset")
                continue

            min_len = min(
                len(psi_analytical),
                len(psi_euler),
                len(psi_euler_improved),
                len(psi_rk4)
            )

            if min_len == 0:
                print(f"Warning: empty data for {col}")
                continue

            psi_analytical = psi_analytical[:min_len]

            # --- Errors ---
            error_euler = psi_euler[:min_len] - psi_analytical
            error_euler_improved = psi_euler_improved[:min_len] - psi_analytical
            error_rk4 = psi_rk4[:min_len] - psi_analytical

            # --- Clean invalid values ---
            def clean(arr):
                arr = arr[np.isfinite(arr)]
                return arr

            error_euler = clean(error_euler)
            error_euler_improved = clean(error_euler_improved)
            error_rk4 = clean(error_rk4)

            # --- Check empty after cleaning ---
            if len(error_euler) == 0 or len(error_euler_improved) == 0 or len(error_rk4) == 0:
                print(f"Warning: no valid data after cleaning for {col}")
                continue

            # --- Compute stats ---
            def compute_stats(error):
                std = np.std(error)
                stderr = std / np.sqrt(len(error))
                return std, stderr

            std_euler, stderr_euler = compute_stats(error_euler)
            std_euler_improved, stderr_euler_improved = compute_stats(error_euler_improved)
            std_rk4, stderr_rk4 = compute_stats(error_rk4)

            results[col] = {
                "Euler": {"std": std_euler, "stderr": stderr_euler},
                "Euler Improved": {"std": std_euler_improved, "stderr": stderr_euler_improved},
                "RK4": {"std": std_rk4, "stderr": stderr_rk4}
            }

        return results

    except Exception as e:
        print(f"Unexpected error in compare_methods: {e}")
        return None
=======
import numpy as np
import pandas as pd

from compute_analytical import compute_psi
from compute_euler import compute_euler
from compute_euler_improved import compute_euler_improved
from compute_rk4 import compute_rk4


def compare_methods(data_analytical, data_euler, data_euler_improved, data_rk4):
    """
    Compare methods and compute statistics for each n.

    Returns:
    --------
    dict:
        {
            "n=1": {
                "std": value,
                "stderr": value
            },
            ...
        }
    """

    results = {}

    # Get list of n columns
    n_columns = [col for col in data_analytical.columns if col != "x"]

    for col in n_columns:
        psi_analytical = data_analytical[col].values
        psi_euler = data_euler[col].values
        psi_euler_improved = data_euler_improved[col].values
        psi_rk4 = data_rk4[col].values

        # Align lengths
        min_len = min(
            len(psi_analytical),
            len(psi_euler),
            len(psi_euler_improved),
            len(psi_rk4)
        )

        # Stack values for comparison
        values = np.vstack([
            psi_analytical[:min_len],
            psi_euler[:min_len],
            psi_euler_improved[:min_len],
            psi_rk4[:min_len]
        ])

        # Compute statistics across methods
        std = np.std(values, axis=0)          # std per x
        stderr = std / np.sqrt(values.shape[0])  # standard error

        # Aggregate (mean of std over domain)
        results[col] = {
            "mean_std": np.mean(std),
            "mean_stderr": np.mean(stderr)
        }

    return results
>>>>>>> 7184de9 (Added banner, changed readme)
