from compute_rk4 import compute_rk4
from plot_rk4 import plot

data = compute_rk4()
chosen_n = int(input("Enter which n to plot: "))
plot(data, chosen_n)