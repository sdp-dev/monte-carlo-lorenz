# Monte Carlo Simulation for Lorenz Curve

## Description

This project simulates and graphs the Lorenz curve using Monte Carlo methods to estimate the Gini coefficient, a key measure of economic inequality. Users can input their data points to define the curve or use default points. The simulation generates random points, compares them with the curve, and calculates the Gini coefficient.

## Features

- **Customizable Lorenz Curve:**
  - Allows users to input custom points.
  - Uses default points if none are provided.

- **Monte Carlo Simulation:**
  - Generates random points to compare against the curve.
  - Calculates the area under the curve to estimate the Gini coefficient.

- **Data Visualization:**
  - Visualizes the Lorenz curve with color-coded points based on whether they are above or below the curve.

## Getting Started

### Prerequisites

- Python 3.x
- Required Python libraries:
  - `matplotlib`

### Installing

1. Clone the repository:

    ```bash
    git clone <https://github.com/sdp-dev/monte-carlo-lorenz.git>
    ```

2. Install the required dependencies:

    ```bash
    pip install matplotlib
    ```

## Usage

1. Run the main Python script:

    ```bash
    python montecarlo.py
    ```

2. Enter the Lorenz curve points in the format `x,y`, separated by commas. Type `done` to finish inputting points.

3. View the graph, which shows the Lorenz curve and color-coded points from the Monte Carlo simulation.
