import pandas as pd
import json

# Read the CSV file
df = pd.read_csv('/Users/nghiempt/Src/Research/conf_a&p_2025/scenario/case-07/data/450-train-llm.csv')

# Function to extract the values from the result column
def extract_result_values(result):
    result_dict = json.loads(result.replace("'", "\""))
    return pd.Series([result_dict.get('incorrect', 0), result_dict.get('incomplete', 0), result_dict.get('inconsistent', 0)])

# Apply the function to the result column
df[['incorrect', 'incomplete', 'inconsistent']] = df['result'].apply(extract_result_values)

# Drop the original result column
df = df.drop(columns=['result'])

# Export the modified DataFrame to a new CSV file
df.to_csv('/Users/nghiempt/Src/Research/conf_a&p_2025/scenario/case-07/data/450-train-llm-process.csv', index=False)

print("CSV file has been successfully created.")