import pandas as pd
import numpy as np
import sys

# Get input/output file paths from Snakemake
input_file = sys.argv[1]
output_file = sys.argv[2]

# Read the data
df = pd.read_csv(input_file)

# Remove the largest outlier in 'Balance'
threshold = df['Balance'].mean() + 3 * df['Balance'].std()
df_cleaned = df[df['Balance'] < threshold]

# Save the cleaned data
df_cleaned.to_csv(output_file, index=False)
