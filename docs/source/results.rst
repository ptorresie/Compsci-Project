Results Interpretation
======================

The numerical comparison highlights clear differences in accuracy
between the implemented methods.

The Euler method exhibits the largest deviation from the analytical
solution. This is expected due to its first-order approximation,
which accumulates truncation error at each step.

The Improved Euler method reduces this error by incorporating
an additional slope estimate, resulting in noticeably better accuracy.
However, some deviation remains, particularly for larger step sizes.

The Runge-Kutta 4 (RK4) method provides the closest approximation
to the analytical solution. Its higher-order formulation significantly
reduces both local and global truncation errors.

Statistical analysis further supports these observations:

- The standard deviation of RK4 results is consistently lower,
  indicating higher stability.
- The standard error confirms that RK4 produces the most reliable
  approximation across all tested values of \( n \).

Overall, the results demonstrate the trade-off between computational
complexity and accuracy, with RK4 offering the best performance
at the cost of increased computation.

These findings align with theoretical expectations from numerical
analysis, confirming the effectiveness of higher-order methods
in solving differential equations.