import numpy as np
import pytest

from src.stage5_comparison.compare_methods import compare_methods
from src.stage5_comparison.main_v5 import run_comparison

from src.stage1_analytical.compute_analytical import compute_psi
from src.stage2_euler.compute_euler import compute_euler
from src.stage3_euler_improved.compute_euler_improved import compute_euler_improved
from src.stage4_rk4.compute_rk4 import compute_rk4


# =========================
# TEST DATA
# =========================

def get_test_data():
    return {
        "n_start": 1,
        "n_end": 2,
        "n_step": 1,
        "h": 0.1,
        "num_steps": 100,
        "L": 10,
        "z0": 0.1,
        "psi0": 0.0,
    }


# =========================
# TEST 1: COMPUTE FUNCTIONS
# =========================

def test_compute_functions_return_dataframe():
    data = get_test_data()

    analytical = compute_psi(L=data["L"], dx=data["h"], n_values=np.array([1, 2]))
    euler = compute_euler({
        "n_start": data["n_start"],
        "n_end": data["n_end"],
        "n_step": data["n_step"],
        "delta_x": data["h"],
        "num_steps": data["num_steps"],
        "L": data["L"],
        "z_0": data["z0"],
        "psi_0": data["psi0"],
    })
    improved = compute_euler_improved(data)
    rk4 = compute_rk4(data)

    assert analytical is not None
    assert euler is not None
    assert improved is not None
    assert rk4 is not None


# =========================
# TEST 2: COMPARE STRUCTURE
# =========================

def test_compare_returns_dict():
    data = get_test_data()

    analytical = compute_psi(L=data["L"], dx=data["h"], n_values=np.array([1, 2]))
    euler = compute_euler({
        "n_start": data["n_start"],
        "n_end": data["n_end"],
        "n_step": data["n_step"],
        "delta_x": data["h"],
        "num_steps": data["num_steps"],
        "L": data["L"],
        "z_0": data["z0"],
        "psi_0": data["psi0"],
    })
    improved = compute_euler_improved(data)
    rk4 = compute_rk4(data)

    results = compare_methods(analytical, euler, improved, rk4)

    assert isinstance(results, dict)


# =========================
# TEST 3: COMPARE VALIDITY
# =========================

def test_compare_values_are_finite():
    data = get_test_data()

    analytical = compute_psi(L=data["L"], dx=data["h"], n_values=np.array([1, 2]))
    euler = compute_euler({
        "n_start": data["n_start"],
        "n_end": data["n_end"],
        "n_step": data["n_step"],
        "delta_x": data["h"],
        "num_steps": data["num_steps"],
        "L": data["L"],
        "z_0": data["z0"],
        "psi_0": data["psi0"],
    })
    improved = compute_euler_improved(data)
    rk4 = compute_rk4(data)

    results = compare_methods(analytical, euler, improved, rk4)

    for n, methods in results.items():
        for method, stats in methods.items():
            assert np.isfinite(stats["std"])
            assert np.isfinite(stats["stderr"])


# =========================
# TEST 4: COMPARE ERROR HANDLING
# =========================

def test_compare_handles_none():
    results = compare_methods(None, None, None, None)
    assert results is None


# =========================
# TEST 5: FULL PIPELINE (NEW main_v5)
# =========================

def test_run_comparison_returns_dict():
    results = run_comparison(get_test_data())
    assert isinstance(results, dict)


# =========================
# TEST 6: FULL PIPELINE VALIDITY
# =========================

def test_run_comparison_values_are_finite():
    results = run_comparison(get_test_data())

    for n, methods in results.items():
        for method, stats in methods.items():
            assert np.isfinite(stats["std"])
            assert np.isfinite(stats["stderr"])


# =========================
# TEST 7: FULL PIPELINE ERROR HANDLING
# =========================

def test_run_comparison_invalid_input():
    data = get_test_data()
    data["n_start"] = 5
    data["n_end"] = 1  # invalid

    results = run_comparison(data)

    assert results is None