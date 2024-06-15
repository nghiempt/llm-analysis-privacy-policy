import json

input_json_file = 'scenario/case-02/data/150-train-actual.json'

output_jsonl_file = 'scenario/case-02/data/150-train-actual.jsonl'

with open(input_json_file, 'r') as json_file, open(output_jsonl_file, 'w') as jsonl_file:
    data = json.load(json_file)
    
    for item in data:
        jsonl_file.write(json.dumps(item) + '\n')
