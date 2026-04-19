from euler2 import compute_euler
from plot_euler import plot

data = compute_euler()
chosen_n = int(input("Enter which n to plot: "))
plot(data, chosen_n)