import numpy as np
import pandas as pd
import pytest

from src.stage1_analytical.compute_analytical import compute_psi
from src.stage1_analytical.plot_analytical import plot


# =========================
# TEST GROUP 1: STRUCTURE
# =========================

def test_returns_dataframe():
    df = compute_psi(L=10, dx=1, n_values=np.array([1]))
    assert isinstance(df, pd.DataFrame)


def test_contains_x_column():
    df = compute_psi(L=10, dx=1, n_values=np.array([1]))
    assert "x" in df.columns


def test_correct_n_columns():
    n_vals = np.array([1, 2, 3])
    df = compute_psi(L=10, dx=1, n_values=n_vals)

    for n in n_vals:
        assert f"n={n}" in df.columns


# =========================
# TEST GROUP 2: SHAPE
# =========================

def test_shape_consistency():
    L = 10
    dx = 1
    n_vals = np.array([1, 2])

    df = compute_psi(L=L, dx=dx, n_values=n_vals)

    expected_rows = len(np.arange(0, L + dx, dx))
    expected_cols = len(n_vals) + 1  # +1 for 'x'

    assert df.shape == (expected_rows, expected_cols)


# =========================
# TEST GROUP 3: PHYSICS
# =========================

def test_boundary_conditions():
    L = 10
    df = compute_psi(L=L, dx=1, n_values=np.array([1]))

    psi_0 = df["n=1"].iloc[0]
    psi_L = df["n=1"].iloc[-1]

    assert abs(psi_0) < 1e-10
    assert abs(psi_L) < 1e-10


def test_known_value():
    """
    For n=1 and x ≈ L/2:
    ψ ≈ sqrt(2/L)
    """
    L = 10
    dx = 1

    df = compute_psi(L=L, dx=dx, n_values=np.array([1]))

    # Use midpoint index instead of exact float match
    psi_val = df.iloc[len(df)//2]["n=1"]
    expected = np.sqrt(2 / L)

    assert abs(psi_val - expected) < 1e-6


# =========================
# TEST GROUP 4: INPUT HANDLING
# =========================

def test_no_user_input_required():
    df = compute_psi(L=10, dx=1, n_values=np.array([1, 2]))
    assert df is not None
    assert not df.empty


# =========================
# TEST GROUP 5: PLOT FUNCTION
# =========================

def test_plot_valid_n():
    df = compute_psi(L=10, dx=1, n_values=np.array([1]))
    plot(df, 1)  # should not raise error


def test_plot_invalid_n():
    df = compute_psi(L=10, dx=1, n_values=np.array([1]))

    with pytest.raises(ValueError):
        plot(df, 5)


# =========================
# TEST GROUP 6: ERROR HANDLING
# =========================

def test_invalid_L():
    df = compute_psi(L=-10, dx=1, n_values=np.array([1]))
    assert df is None


def test_invalid_dx():
    df = compute_psi(L=10, dx=0, n_values=np.array([1]))
    assert df is None


def test_empty_n_values():
    df = compute_psi(L=10, dx=1, n_values=np.array([]))
    assert df is None