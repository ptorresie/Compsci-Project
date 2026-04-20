import numpy as np
import pandas as pd
import pytest

from src.stage2_euler.compute_euler import compute_euler
from src.stage2_euler.plot_euler import plot


# =========================
# 🔹 TEST GROUP 1: STRUCTURE
# =========================

def get_test_data():
    return {
        "n_start": 1,
        "n_end": 2,
        "n_step": 1,
        "delta_x": 0.1,
        "num_steps": 100,
        "L": 10,
        "z_0": 0.1,
        "psi_0": 0.0,
    }


def test_returns_dataframe():
    df = compute_euler(get_test_data())
    assert isinstance(df, pd.DataFrame)


def test_contains_x_column():
    df = compute_euler(get_test_data())
    assert "x" in df.columns


def test_correct_n_columns():
    df = compute_euler(get_test_data())

    assert "n=1" in df.columns
    assert "n=2" in df.columns


# =========================
# 🔹 TEST GROUP 2: SHAPE
# =========================

def test_shape_consistency():
    data = get_test_data()
    df = compute_euler(data)

    expected_rows = data["num_steps"]
    expected_cols = (data["n_end"] - data["n_start"] + 1) + 1

    assert df.shape == (expected_rows, expected_cols)


# =========================
# 🔹 TEST GROUP 3: PHYSICS / BEHAVIOR
# =========================

def test_initial_condition():
    df = compute_euler(get_test_data())

    # psi_0 = 0 → first row should be zero
    assert abs(df["n=1"].iloc[0]) < 1e-10


def test_no_nan_values():
    df = compute_euler(get_test_data())

    assert not df.isnull().values.any()


def test_values_are_finite():
    df = compute_euler(get_test_data())

    assert np.isfinite(df.values).all()


# =========================
# 🔹 TEST GROUP 4: DOMAIN
# =========================

def test_x_values_start_at_zero():
    df = compute_euler(get_test_data())

    assert df["x"].iloc[0] == 0


def test_x_values_increase():
    df = compute_euler(get_test_data())

    x = df["x"].values
    assert np.all(np.diff(x) > 0)


# =========================
# 🔹 TEST GROUP 5: PLOT FUNCTION
# =========================

def test_plot_valid_n():
    df = compute_euler(get_test_data())

    # Should NOT raise error
    plot(df, 1)


def test_plot_invalid_n():
    df = compute_euler(get_test_data())

    with pytest.raises(ValueError):
        plot(df, 99)