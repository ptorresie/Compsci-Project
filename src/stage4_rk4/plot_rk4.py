import matplotlib.pyplot as plt

def plot(data, chosen_n):
    column_name = f"n={chosen_n}"

    if column_name not in data.columns:
        raise ValueError(f"{column_name} not found in data")

    x_values = data["x"]
    psi_values = data[column_name]

    plt.figure(figsize=(10, 5))
    plt.plot(x_values, psi_values)
    plt.xlabel("x")
    plt.ylabel("ψ(x)")
    plt.title(f"RK4 solution for n = {chosen_n}")
    plt.grid(True)
    plt.show()