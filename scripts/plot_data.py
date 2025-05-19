import pandas as pd
import matplotlib.pyplot as plt
import sys

# Get file paths
input_file = sys.argv[1]
output_file = sys.argv[2]

# Read the cleaned data
df = pd.read_csv(input_file)

# Plot it (assuming 'Day' and 'Balance' columns)
plt.figure(figsize=(10, 6))
plt.plot(df['Day'], df['Balance'], marker='o', color='blue')
plt.title("Bank Account Balance Over Time")
plt.xlabel("Day")
plt.ylabel("Balance")
plt.grid(True)

# Save the graph
plt.savefig(output_file)
