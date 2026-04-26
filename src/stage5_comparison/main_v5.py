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

    status = {
        "Analytical": True,
        "Euler": True,
        "Euler Improved": True,
        "RK4": True,
        "Comparison": True
    }

    try:
        # unpack parameters
        n_start = params["n_start"]
        n_end = params["n_end"]
        n_step = params["n_step"]
        L = params["L"]
        h = params["h"]
        num_steps = params["num_steps"]
        z0 = params["z0"]
        psi0 = params["psi0"]

        n_values = np.arange(n_start, n_end + 1, n_step)

        # --- COMPUTE ---
        data_analytical = compute_psi(L=L, dx=h, n_values=n_values)
        if data_analytical is None:
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

        # --- COMPARE ---
        if any(d is None for d in [data_analytical, data_euler, data_euler_improved, data_rk4]):
            status["Comparison"] = False
            return None

        results = compare_methods(
            data_analytical,
            data_euler,
            data_euler_improved,
            data_rk4
        )

        return results

    except Exception:
        return None