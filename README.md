# Quantum Numerical Methods Project

## Description

This project studies the time-independent Schrödinger equation for a particle confined in a one-dimensional infinite potential well.

The governing equation is:

−(ħ² / 2m) d²ψ/dx² = Eψ

For this system, the analytical solution (particle in a box) is:

ψₙ(x) = √(2 / L) · sin(nπx / L)

This exact solution is used as a reference to evaluate numerical approximations.

The project implements and compares the following numerical methods:

* Euler method (first-order approximation)
* Improved Euler (Heun method)
* Runge–Kutta 4 (RK4)

Each method approximates the wave function ψ(x) over a discretized domain (x ∈ [0, L]) and is evaluated in terms of accuracy and stability.

---

## Installation

1. Clone the repository:

git clone https://github.com/ptorresie/Compsci-Project.git
cd Compsci-Project

2. Create and activate the environment:

conda env create -f environment.yml
conda activate <env_name>

---

## Usage

Run the program from the project root:

(from the Compsci-Project level):
PYTHONPATH=. python -m src.main

---

## Instructions

1. Enter the required parameters when prompted:

    Starting and ending quantum numbers (n)
    Step size (h)
    Well length (L)
    Number of steps
    Initial conditions psi0 (ψ₀) and z₀

2. The program will:

    Compute the analytical and numerical solutions

    Compare the methods using statistical measures (standard deviation and error) of the endpoints and their midpoint to reduce redundancy and improve clarity, only representative quantum numbers (minimum, median, and maximum) are selected for comparison
   
    Optionally display a plot showing all methods together

---

## Notes

 The Schrödinger equation is transformed into a system of first-order equations to allow numerical integration.
 Smaller step sizes improve accuracy but increase computation time.
 Euler is less stable, while RK4 provides the most accurate approximation.
 Input validation is implemented to ensure robustness and prevent runtime errors.

---
