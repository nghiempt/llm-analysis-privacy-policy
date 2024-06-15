#### Table of contents
1. [Introduction](#1)
2. [Datasets & Models](#2)
	- [Datasets](#datasets)
	- [Models](#models)
3. [Implementation](#3)
4. [Evaluation](#4)
5. [Example](#5)

# <a name="1"></a> Unveiling Discrepancies in Android App Data Safety Declarations and Privacy Policies: An In-depth Analysis using Large Language Models

## Abstract

This paper investigates the critical inconsistencies observed between data safety declarations and privacy policies on the Android platform, highlighting prevalent ‘incomplete’ and ‘incorrect’ issues. Such misalignments undermine user trust and pose substantial ethical and legal challenges. Our research represents a pioneering effort in this field, raising essential questions about the potential of an approach to address these disparities. We specifically explore whether advanced techniques—namely, fine-tuning large language models (LLMs) such as Gemini 1.5, ChatGPT 3.5, 4, and 4o—could supplant the role of experts. Furthermore, we expand different labeling strategies by LLMs during training to assess whether this increases accuracy and to examine potential hallucination issues that may impact the classification. To this end, we implement four scenarios across eight cases: i) zero-shot by ChatGPT 3.5; ii) manual label fine-tuning by ChatGPT 3.5; iii) fine-tuning with 150 apps using labels generated by ChatGPT 4, ChatGPT 4o, and Gemini 1.5; and iv) fine-tuning with 450 apps using labels from these platforms. Our findings indicate that while the zero-shot LLM scenario showed variable accuracy (ranging from 57% to 79%), manual label fine-tuning yielded promising results with accuracies between 84% and 95%. Fine-tuning with LLM-generated labels for 150 apps resulted in accuracies ranging from 76% to 94% with the best outcome of Gemini 1.5. Notably, when scaling up to 450 apps, the accuracy remained stable for ChatGPT 4o and Gemini models. Still, it declined slightly from 76% to 73% for the ChatGPT 4 model for the ‘incorrect’ classification, likely due to hallucination effects caused by inadequate training data. Committed to transparency and advancing research in this domain, we release a benchmark dataset and maintain a list of the analyzed 600 Android apps.


## Software implementation

> Briefly describe the software that was written to produce the results of this
> paper.

All source code used to generate the results and figures in the paper are in
the `code` folder.
The calculations and figure generation are all run inside
[Jupyter notebooks](http://jupyter.org/).
The data used in this study is provided in `data` and the sources for the
manuscript text and figures are in `manuscript`.
Results generated by the code are saved in `results`.
See the `README.md` files in each directory for a full description.

## License

All Python source code (including .py and .ipynb files) is made available under the MIT license. You can freely use and modify the code, without warranty, so long as you provide attribution to the authors. See LICENSE for the full license text.

# <a name="2"></a> Datasets & Models

## Datasets <a name="datasets"></a>

|App ID|App Name|App Package|Incorrect|Incomplete|
| ------------- | -------------  | ------------- | ------------- | ------------- |
| 1             | aaa | com.aaa | 0 | 0 |
| 1             | aaa | com.aaa | 0 | 0 |
| 1             | aaa | com.aaa | 0 | 0 |
| 1             | aaa | com.aaa | 0 | 0 |
| 1             | aaa | com.aaa | 0 | 0 |
| 1             | aaa | com.aaa | 0 | 0 |

|Category|Number of apps|#|Number of downloads|Number of apps|
|---|---|---|---|---|
|aaa|0 apps|#|100 - 1000|0 apps|
|aaa|0 apps|#|100 - 1000|0 apps|
|aaa|0 apps|#|100 - 1000|0 apps|

## Models <a name="models"></a>

|Model|Params|
|---|---|
|aaa|100B|
|aaa|100B|
|aaa|100B|

# <a name="3"></a> Implementation

![alt text](https://github.com/nghiempt/llm-analysis-privacy-policy/blob/master/implementation.jpg)

## Case 01: ask gpt-3.5-turbo to get answer (zero-shot)
 - Step 01: run file zero-shot.py with data 150-test-none.csv, after we get file 150-test-zr.csv.
 - Step 02: run file process-outcome.py with data 150-test-zr.csv to format output to each column csv, after we get file 150-test-zr-process.csv.
 - Step 03: run file evaluation.ipynb to compare value between actual and predict, after we get the matric and save in file report.txt.

## Case 02: fine-tuning gpt-3.5-turbo with manual data
 - Step 01: run file convert-csv-to-json.py with data 150-train-actual.csv to transfer data from csv to json format.
 - Step 02: run file convert-json-to-jsonl to convert previous file json to jsonl (fine tune need jsonl format).
 - Step 03: fine-tuning (we use Postman to call api openai for this process), after we get the model ID fine tuned with our data.
 - Step 04: run file test-fine-tuned-model.py with model ID fine tuned and data 150-test-none.csv, after we get file 150-test-ft.csv.
 - Step 05: run file process-outcome.py with data 150-test-ft.csv to format output to each column csv, after we get file 150-test-ft-process.csv.
 - Step 06: run file evaluation.ipynb to compare value between actual and predict, after we get the matric and save in file report.txt.

## Case 03: fine-tuning gpt-3.5-turbo with data labeled by LLM
 - Step 01: run file llm-label.py with data 150-train-need.csv to get label by LLM, after we get file 150-train-llm.csv.
 - Step 02: run file process-outcome-label.py with data 150-train-llm.csv to format output to each column csv, after we get file 150-train-llm-process.csv.
 - Step 03: run file convert-csv-to-json.py with data 150-train-llm-process.csv to transfer data from csv to json format.
 - Step 04: run file convert-json-to-jsonl to convert previous file json to jsonl (fine tune need jsonl format).
 - Step 05: fine-tuning (we use Postman to call api openai for this process), after we get the model ID fine tuned with our data.
 - Step 06: run file test-fine-tuned-model.py with model ID fine tuned and data 150-test-none.csv, after we get file 150-test-ft.csv.
 - Step 07: run file process-outcome-ft.py with data 150-test-ft.csv to format output to each column csv, after we get file 150-test-ft-process.csv.
 - Step 08: run file evaluation.ipynb to compare value between actual and predict, after we get the matric and save in file report.txt.

## FINE TUNING OPENAI (https://platform.openai.com/docs/guides/fine-tuning)

Detail step in file: fine-tuning.txt

# <a name="4"></a> Evaluation

![alt text](https://github.com/nghiempt/llm-analysis-privacy-policy/blob/master/evaluation.jpg)

# <a name="5"></a> Example
 - AppID: 206
 - AppName: Miss International
 - AppPkg: com.choicely.miss.international
 - Data Safety URL: https://play.google.com/store/apps/datasafety?id=com.choicely.miss.international
 - Privacy Policy URL: https://www.miss-international.org/en/privacy/

```
system: You are an expert in analyzing the correctness, completeness, and consistency between the Privacy Policy and Data Safety information provided by Android applications.
user: Let's compare and analyze the information between Data Safety and Privacy Policy to clarify 2 issues: which information is incorrect and which information is incomplete. 
Notes when classifying: 
Incomplete: Data Safety provides information but is not as complete as the Privacy Policy provides. 
Incorrect: Data Safety does not provide that information, but the Privacy Policy mentions it. 
Note: always gives me the result (0 or 1, 1 is yes, 0 is no) in the form below: {'incorrect': (0 or 1), 'incomplete': (0 or 1)}. 
Please in the answer, just give me the json only and in English. Below is information for 2 parts: 
Data Safety: {'data_shared': [], 'data_collected': [{'category': 'Personal info', 'sub_info': [{'data_type': 'Name', 'purpose': 'Account management', 'optional': True}, {'data_type': 'Email address', 'purpose': 'Account management', 'optional': True}]}, {'category': 'Device or other IDs', 'sub_info': [{'data_type': 'Device or other IDs', 'purpose': 'Analytics', 'optional': False}]}, {'category': 'App activity', 'sub_info': [{'data_type': 'App interactions', 'purpose': 'Analytics', 'optional': False}]}, {'category': 'App info and performance', 'sub_info': [{'data_type': 'Crash logs', 'purpose': 'Analytics', 'optional': False}, {'data_type': 'Diagnostics', 'purpose': 'Analytics', 'optional': False}, {'data_type': 'Other app performance data', 'purpose': 'Analytics', 'optional': False}]}], 'security_practices': [{'category': 'Data is encrypted in transit', 'sub_info': []}, {'category': 'You can request that data be deleted', 'sub_info': []}]}. 
Privacy Policy: 
Data Share: The content does not specify any explicit data sharing practices, although the community guidelines do point out that comments with personal information leaks will not be deleted. This implies a degree of public information sharing within the community. However, implications of sharing user's information with third parties or other entities aren't mentioned. 
Data Collect: The privacy policy does not specify the types of data it collects from the users. It only states the website is for exchanging information and news about Miss International and user comments will not be deleted. While it doesn't specifically detail the type of user information it collects, the mention of not deleting comments containing personal information leaks suggests that user comments might be stored. Also, if users are engaging through comments, it might be inferred that user data such as username or user ID could be collected.

```
```
{
    "model": "gpt-4",
    "messages": [
        {
            "role": "system",
            "content": system
        },
        {
            "role": "user",
            "content": user
        }
    ],
    "temperature": 0.7
}
```

```
{
    "id": "chatcmpl-9axxxxxxxxxx",
    "object": "chat.completion",
    "created": 1718439928,
    "model": "gpt-4-0613",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "{'incorrect': 1, 'incomplete': 1}"
            },
            "logprobs": null,
            "finish_reason": "stop"
        }
    ],
    "usage": {
        "prompt_tokens": 590,
        "completion_tokens": 13,
        "total_tokens": 603
    },
    "system_fingerprint": null
}
```
