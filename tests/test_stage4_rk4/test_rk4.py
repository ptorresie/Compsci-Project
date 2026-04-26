import numpy as np
import pandas as pd
import pytest

from src.stage4_rk4.compute_rk4 import compute_rk4
from src.stage4_rk4.plot_rk4 import plot
from src.stage1_analytical.compute_analytical import compute_psi
from src.stage2_euler.compute_euler import compute_euler


# =========================
# 🔹 TEST DATA
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
# TEST GROUP 1: STRUCTURE
# =========================

def test_returns_dataframe():
    df = compute_rk4(get_test_data())
    assert isinstance(df, pd.DataFrame)


def test_contains_x_column():
    df = compute_rk4(get_test_data())
    assert "x" in df.columns


def test_correct_n_columns():
    df = compute_rk4(get_test_data())

    assert "n=1" in df.columns
    assert "n=2" in df.columns


# =========================
# TEST GROUP 2: SHAPE
# =========================

def test_shape_consistency():
    data = get_test_data()
    df = compute_rk4(data)

    expected_rows = data["num_steps"]
    expected_cols = (data["n_end"] - data["n_start"] + 1) + 1

    assert df.shape == (expected_rows, expected_cols)


# =========================
# TEST GROUP 3: PHYSICS / STABILITY
# =========================

def test_initial_condition():
    df = compute_rk4(get_test_data())
    assert abs(df["n=1"].iloc[0]) < 1e-10


def test_no_nan_values():
    df = compute_rk4(get_test_data())
    assert not df.isnull().values.any()


def test_values_are_finite():
    df = compute_rk4(get_test_data())
    assert np.isfinite(df.values).all()


# =========================
# TEST GROUP 4: DOMAIN
# =========================

def test_x_values_start_at_zero():
    df = compute_rk4(get_test_data())
    assert df["x"].iloc[0] == 0


def test_x_values_increase():
    df = compute_rk4(get_test_data())
    x = df["x"].values
    assert np.all(np.diff(x) > 0)


# =========================
# TEST GROUP 5: ACCURACY
# =========================

def test_rk4_close_to_analytical():
    data = get_test_data()
    L = data["L"]

    df_rk4 = compute_rk4(data)
    df_exact = compute_psi(L=L, dx=data["h"], n_values=np.array([1]))

    psi_rk4 = df_rk4["n=1"].values
    psi_exact = df_exact["n=1"].values

    min_len = min(len(psi_rk4), len(psi_exact))
    error = np.mean(np.abs(psi_rk4[:min_len] - psi_exact[:min_len]))

    assert error < 0.1


# =========================
# TEST GROUP 6: COMPARISON WITH EULER
# =========================

def test_rk4_better_than_euler():
    data_rk4 = get_test_data()

    data_euler = {
        "n_start": 1,
        "n_end": 1,
        "n_step": 1,
        "delta_x": data_rk4["h"],
        "num_steps": data_rk4["num_steps"],
        "L": data_rk4["L"],
        "z_0": data_rk4["z0"],
        "psi_0": data_rk4["psi0"],
    }

    df_rk4 = compute_rk4(data_rk4)
    df_euler = compute_euler(data_euler)
    df_exact = compute_psi(L=data_rk4["L"], dx=data_rk4["h"], n_values=np.array([1]))

    psi_rk4 = df_rk4["n=1"].values
    psi_euler = df_euler["n=1"].values
    psi_exact = df_exact["n=1"].values

    min_len = min(len(psi_rk4), len(psi_exact))

    error_rk4 = np.mean(np.abs(psi_rk4[:min_len] - psi_exact[:min_len]))
    error_euler = np.mean(np.abs(psi_euler[:min_len] - psi_exact[:min_len]))

    assert error_rk4 <= error_euler + 0.02


# =========================
# TEST GROUP 7: ERROR HANDLING
# =========================

def test_invalid_L():
    data = get_test_data()
    data["L"] = -10

    df = compute_rk4(data)
    assert df is None


def test_invalid_h():
    data = get_test_data()
    data["h"] = 0

    df = compute_rk4(data)
    assert df is None


def test_invalid_n_range():
    data = get_test_data()
    data["n_start"] = 10
    data["n_end"] = 1

    df = compute_rk4(data)
    assert df is None


# =========================
# TEST GROUP 8: PLOT FUNCTION
# =========================

def test_plot_valid_n():
    df = compute_rk4(get_test_data())
    plot(df, 1)


def test_plot_invalid_n():
    df = compute_rk4(get_test_data())

    with pytest.raises(ValueError):
        plot(df, 99)