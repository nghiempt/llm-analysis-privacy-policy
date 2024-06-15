import csv
import json

def csv_to_json(csv_file):

  with open(csv_file, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)

    data = []

    for row in reader:
      json_object = {
        "messages": [
          {
                "role": "system",
                "content": "You are an expert in analyzing the correctness, completeness, and consistency between the Privacy Policy and Data Safety information provided by Android applications."
            },
            {
                "role": "user",
                "content": '''Let's compare and analyze the information between Data Safety and Privacy Policy to clarify 3 issues: which information is incorrect, which information is incomplete and which information is inconsistent. Notes when classifying: Incomplete: Data Safety provides information but is not as complete as the Privacy Policy provides. Incorrect: Data Safety does not provide that information, but the Privacy Policy mentions it. Inconsistency: Data Safety is provided but its description is inconsistent with the Privacy Policy information provided. Note: always gives me the result (0 or 1, 1 is yes, 0 is no) in the form below: {"incorrect": (0 or 1), "incomplete": (0 or 1), "inconsistent": (0 or 1)}. Please in the answer, just give me the json only and in English. Below is information for 2 parts:\nData Safety: ''' + row['data_safety_content'] + '''\nPrivacy Policy:\n''' + row['privacy_policy_content'] + ''' '''
            },
            {
                "role": "assistant",
                "content": '''{"incorrect": '''+ row['incorrect'] +''', "incomplete": '''+ row['incomplete'] +''', "inconsistent": '''+ row['inconsistent'] +'''}'''
            }
        ],
      }

      data.append(json_object)

  with open('scenario/case-04/data/150-train-llm-process.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(data, jsonfile, indent=4)

csv_file = 'scenario/case-04/data/150-train-llm-process.csv'
csv_to_json(csv_file)

print("JSON file 'app_data.json' created successfully.")
