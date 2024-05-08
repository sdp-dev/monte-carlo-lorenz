import matplotlib.pyplot as plt
import random

# Method to collect user input to graph Lorenz curve
def get_user_input_points():
    points = []
    print("Enter points for the Lorenz curve as comma-separated pairs (e.g., 0,0). Enter 'done' when finished:")
    while True:
        user_input = input("Enter a point (or 'done'): ").strip()
        if user_input.lower() == 'done':
            break
        try:
            x, y = map(float, user_input.split(","))
            points.append((x, y))
        except ValueError:
            print("Invalid input. Please enter a valid comma-separated pair of numbers.")
    return sorted(points)  # Ensure points are sorted by x-values

# Interpolate Lorenz curve by calculating slope of lines connecting given points
def interpolate_lorenz_curve(x, lorenz_points):
    left_point = max((xval, yval) for (xval, yval) in lorenz_points if xval <= x)
    right_point = min((xval, yval) for (xval, yval) in lorenz_points if xval >= x)
    slope = (right_point[1] - left_point[1]) / (right_point[0] - left_point[0])
    return left_point[1] + slope * (x - left_point[0])

# Main method to collect user input, build curve, and applying Monte Carlo simulation
def main():
    lorenz_points = get_user_input_points()
    if not lorenz_points:
        print("No points provided. Using default Lorenz points.")
        lorenz_points = [(0, 0), (10, 1.882), (20, 5.137), (30, 9.655), (40, 15.410),
                         (50, 22.451), (60, 30.961), (70, 41.094), (80, 53.579),
                         (90, 69.901), (100, 100)]

    num_points = 10000
    points_under_curve = 0
    x_values = []
    y_values = []
    colors = []

    for _ in range(num_points):
        x = random.uniform(0, 100)
        y = random.uniform(0, 100)
        x_values.append(x)
        y_values.append(y)
        if y <= interpolate_lorenz_curve(x, lorenz_points):
            points_under_curve += 1
            colors.append('blue')
        else:
            colors.append('red')

    # Calculate the area under the Lorenz curve (B)
    area_ratio = points_under_curve / num_points

    # Calculate the Gini coefficient using A / (A + B)
    gini_coefficient = (0.5 - area_ratio) / 0.5

    # Plotting the Lorenz curve and the random points
    fig, ax = plt.subplots()
    ax.plot([p[0] for p in lorenz_points], [p[1] for p in lorenz_points], '-o', color='black', label="Lorenz Curve")
    ax.scatter(x_values, y_values, color=colors, alpha=0.5, s=1)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_aspect('equal')
    plt.title("Monte Carlo Simulation: Area Under Lorenz Curve\n", weight='bold')
    ax.set_xlabel("Cumulative share of population (%)")
    ax.set_ylabel("Cumulative share of income (%)")
    ax.legend(loc='upper left')

    # Add annotations below the graph using figure coordinates
    fig.text(0.3, 0.05, f"Area under Lorenz curve (B): {area_ratio:.3f}", fontsize=12, color='black', ha='left')
    fig.text(0.3, 0.1, f"Gini coefficient (A/A+B): {gini_coefficient:.3f}", fontsize=12, color='black', ha='left')

    # Adjust layout to create space for annotations
    plt.tight_layout(rect=[0, 0.15, 1, 1])
    plt.show()

if __name__ == "__main__":
    main()