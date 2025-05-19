import sys
import pandas as pd
import matplotlib.pyplot as plt

input_file = sys.argv[1]
output_file = sys.argv[2]

df = pd.read_csv(input_file)

# Plot the first two numeric columns if available
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
if len(numeric_cols) >= 2:
    plt.figure()
    plt.plot(df[numeric_cols[0]], df[numeric_cols[1]])
    plt.xlabel(numeric_cols[0])
    plt.ylabel(numeric_cols[1])
    plt.title("Sample Line Graph")
    plt.savefig(output_file)
else:
    raise ValueError("Not enough numeric columns to plot.")
