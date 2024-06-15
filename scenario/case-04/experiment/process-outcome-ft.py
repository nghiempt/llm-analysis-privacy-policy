import pandas as pd # type: ignore
import json

df = pd.read_csv('scenario/case-04/data/150-test-ft.csv')

def extract_result_values(result):
    result_dict = json.loads(result.replace("'", "\""))
    return pd.Series([result_dict.get('incorrect', 0), result_dict.get('incomplete', 0), result_dict.get('inconsistent', 0)])

df[['incorrect', 'incomplete', 'inconsistent']] = df['result'].apply(extract_result_values)

df = df.drop(columns=['result'])

df.to_csv('scenario/case-04/data/150-test-ft-process.csv', index=False)

print("CSV file has been successfully created.")