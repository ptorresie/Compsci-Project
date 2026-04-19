Electron Probability Simulation — Numerical Solution of the Schrödinger Equation

Executive Summary:

This project delivers a rigorous computational study of the time‑independent Schrödinger equation for a particle in a one‑dimensional infinite potential well. It combines analytical physics** with numerical methods to compute and analyze the wave function (\psi(x)) and its associated probability density (|\psi(x)|^2).

The system is engineered with a clear separation of concerns: a computation layer for numerical solvers and a visualization layer for scientific interpretation. The outcome is a reproducible, extensible framework to evaluate accuracy, stability, and error behavior across multiple numerical schemes.

---

## Objectives

  Compute the wave function for a particle in a box
  Derive and analyze the probability density
  Implement and benchmark numerical solvers:

   Euler
   Improved Euler (Heun)
   Runge–Kutta 4 (RK4)

  Compare numerical outputs against the analytical solution
  Quantify error propagation and method accuracy

---

## Scientific Foundation

The governing equation is the time‑independent Schrödinger equation in one dimension.

To enable numerical integration, the system is reformulated as two first‑order equations.

The analytical solution for a particle confined in a box of length (L) is displayed in the code.

This solution serves as the ground truth benchmark for all numerical methods implemented.

---

## System Architecture

The project is organized around a staged computational pipeline combined with shared utilities and visualization tools.

## Source Structure (as implemented)

src/
│
├── inputs.py               # Defines global parameters (L, n, step size, etc.)
├── shared_plot.py          # Common plotting utilities used across stages
│
├── compute_analytical.py   # Computes analytical solution ψ(x)
├── plot_analytical.py      # Plots analytical wave function
├── main_v1.py              # Early version of execution pipeline
├── main.py                 # Final integrated execution script
│
├── stage1_analytical/      # Stage 1: Analytical solution
├── stage2_euler/           # Stage 2: Euler method
├── stage3_euler_improved/  # Stage 3: Improved Euler method
├── stage4_rk4/             # Stage 4: Runge-Kutta (RK4)
├── stage5_comparison/      # Stage 5: Method comparison
│
└── utils/                  # Shared computational utilities

Each "stage" folder represents a step in the project development, where a specific numerical or analytical method is implemented and tested independently.

## Stage 1 — Analytical (stage1_analytical)
   Computes the exact solution of the Schrödinger equation
   Serves as the reference baseline for all comparisons

## Stage 2 — Euler (stage2_euler)
   Implements the Euler method
   First numerical approximation of ψ(x)
   Demonstrates initial error behavior

## Stage 3 — Improved Euler (stage3_euler_improved)
   Uses predictor–corrector scheme
   Improves stability and accuracy over basic Euler

## Stage 4 — RK4 (stage4_rk4)
   Implements Runge–Kutta 4th order
   Provides high-precision numerical solution

## Stage 5 — Comparison (stage5_comparison)
   Combines outputs from all methods
   Generates comparative plots
   Used for error and accuracy analysis

## Utility Layer (utils/)

Contains shared logic used across all stages:

   Common mathematical helpers
   Reusable computation logic
   Functions to avoid code duplication

## Visualization Layer

Handled through:

   shared_plot.py → reusable plotting functions
   plot_analytical.py → analytical visualization

These ensure consistent formatting and presentation across all results.

## Execution Flow

inputs.py defines parameters
Each stage computes ψ(x) independently
Results are passed to plotting functions
main.py orchestrates the full pipeline

## Branching Model (Development Strategy)

The repository follows a dual‑branch engineering workflow:

   ## Computations

Focus: numerical correctness and algorithmic implementation

Development of all solvers
Validation against analytical results
Standardization of numerical outputs
   
   ## Plotting

Focus: scientific communication and interpretation

Construction of visual outputs
Comparative analysis tools
Enhancement of clarity and presentation


Both branches converge into main, where integration and final validation occur.


## Functional Overview

The system executes the following pipeline:

  ## Numerical Solution Generation
   Each method computes ψ(x) over a discretized domain

  ## Probability Density Evaluation
   ∣ψ(x)∣^2 is derived directly from computed results

   ## Visualization & Comparison
   Wave functions are plotted
   Probability distributions are visualized
   Numerical methods are benchmarked against the analytical solution


## Numerical Methods — Technical Notes

   ## Euler Method
      First‑order explicit scheme
      Low computational cost
      High cumulative error, especially for oscillatory systems

   ## Improved Euler (Heun)
      Predictor–corrector mechanism
      Reduced truncation error
      Improved stability over basic Euler

   ## Runge–Kutta 4 (RK4)
      Fourth‑order method
      Multiple slope evaluations per step
      High accuracy and stability

## Outputs

The project produces scientifically meaningful visual and numerical outputs:

   Wave function ψ(x) plots
   Probability density ∣ψ(x)∣^2 plots
   Overlay comparisons between analytical and numerical solutions
   Data suitable for further statistical or error analysis

## Final Remarks

This project bridges quantum physics theory and computational methods, demonstrating how numerical analysis can approximate complex physical systems with high precision. It highlights the importance of method selection, parameter tuning, and validation against analytical solutions in scientific computing.