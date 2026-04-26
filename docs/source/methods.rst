Numerical Methods
=================

Euler Method
------------

The Euler method approximates derivatives using:

.. math::

    y_{n+1} = y_n + h f(x_n, y_n)

This method is simple but accumulates error quickly.

Improved Euler Method
---------------------

An improved version of Euler that reduces error by averaging slopes.

Runge-Kutta 4 (RK4)
-------------------

RK4 is a higher-order method that significantly improves accuracy
by combining multiple slope estimates.


Comparison of Methods
---------------------

- Euler: simple but inaccurate
- Improved Euler: better approximation
- RK4: highest accuracy with higher computational cost