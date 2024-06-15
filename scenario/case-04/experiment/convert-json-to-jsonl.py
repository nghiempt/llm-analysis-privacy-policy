import json

input_json_file = 'scenario/case-04/data/150-train-llm-process.json'

output_jsonl_file = 'scenario/case-04/data/150-train-llm-process.jsonl'

with open(input_json_file, 'r') as json_file, open(output_jsonl_file, 'w') as jsonl_file:
    data = json.load(json_file)
    
    for item in data:
        jsonl_file.write(json.dumps(item) + '\n')
