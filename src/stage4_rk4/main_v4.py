from RK4 import compute_rk4
from RK4_plot import plot

data = compute_rk4()
chosen_n = int(input("Enter which n to plot: "))
plot(data, chosen_n)