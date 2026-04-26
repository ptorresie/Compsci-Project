import numpy as np

from src.stage5_comparison.compare_methods import compare_methods

from src.stage1_analytical.compute_analytical import compute_psi
from src.stage2_euler.compute_euler import compute_euler
from src.stage3_euler_improved.compute_euler_improved import compute_euler_improved
from src.stage4_rk4.compute_rk4 import compute_rk4


def run_comparison(params):
    """
    Run full numerical simulation and comparison.

    Parameters
    ----------
    params : dict
        Contains:
        n_start, n_end, n_step, L, h, num_steps, z0, psi0

    Returns
    -------
    dict or None
        Comparison results or None if failure
    """

    try:
        # --- SAFE PARAMETER UNPACKING ---
        try:
            n_start = params["n_start"]
            n_end = params["n_end"]
            n_step = params["n_step"]
            L = params["L"]
            h = params["h"]
            num_steps = params["num_steps"]
            z0 = params["z0"]
            psi0 = params["psi0"]
        except KeyError as e:
            print(f"Missing parameter: {e}")
            return None

        # --- LOGICAL VALIDATION ---
        if n_step <= 0 or h <= 0 or num_steps <= 1 or L <= 0:
            print("Invalid parameter values")
            return None

        if n_start > n_end:
            print("Invalid n range")
            return None

        n_values = np.arange(n_start, n_end + 1, n_step)

        # --- COMPUTE ---
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

        # --- CHECK COMPUTATIONS ---
        if any(d is None for d in [data_analytical, data_euler, data_euler_improved, data_rk4]):
            print("One or more methods failed. Skipping comparison.")
            return None

        # --- COMPARE ---
        results = compare_methods(
            data_analytical,
            data_euler,
            data_euler_improved,
            data_rk4
        )

        return results

    except Exception as e:
        print(f"Unexpected error in run_comparison: {e}")
        return None