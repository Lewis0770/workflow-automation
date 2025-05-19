import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

df = pd.read_csv(input_file)

# Remove rows with extremely high values in a column (example: values > 10000 in last column)
df_cleaned = df[df.iloc[:, -1] < 10000]

df_cleaned.to_csv(output_file, index=False)
