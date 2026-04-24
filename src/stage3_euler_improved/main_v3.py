from compute_euler_improved import compute_euler_improved
from plot_euler_improved import plot

data = compute_euler_improved()
print(data)
chosen_n = int(input("Enter which n to plot: "))
plot(data, chosen_n)