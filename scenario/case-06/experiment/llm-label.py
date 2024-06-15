import asyncio
import csv
import openai
import os
from dotenv import load_dotenv


class HANDLER:
    @staticmethod
    def remove_empty_lines(content):
        lines = content.split("\n")
        cleaned_lines = [line.strip() for line in lines if line.strip()]
        return "\n".join(cleaned_lines)

    @staticmethod
    def ask_gpt(data_safety_content, privacy_policy_content):
        print('''Let's compare and analyze the information between Data Safety and Privacy Policy to clarify 3 issues: which information is incorrect, which information is incomplete and which information is inconsistent. Notes when classifying: Incomplete: Data Safety provides information but is not as complete as the Privacy Policy provides. Incorrect: Data Safety does not provide that information, but the Privacy Policy mentions it. Inconsistency: Data Safety is provided but its description is inconsistent with the Privacy Policy information provided. Note: always gives me the result (0 or 1, 1 is yes, 0 is no) in the form below: {"incorrect": (0 or 1), "incomplete": (0 or 1), "inconsistent": (0 or 1)}. Please in the answer, just give me the json only and in English. Below is information for 2 parts:\nData Safety: ''' + data_safety_content + '''\nPrivacy Policy:\n''' + privacy_policy_content + ''' ''')
        try:
            prompt_message = [
                {
                    "role": "system",
                    "content": "You are an expert in analyzing the correctness, completeness, and consistency between the Privacy Policy and Data Safety information provided by Android applications.",
                },
                {
                    "role": "user",
                    "content": '''Let's compare and analyze the information between Data Safety and Privacy Policy to clarify 3 issues: which information is incorrect, which information is incomplete and which information is inconsistent. Notes when classifying: Incomplete: Data Safety provides information but is not as complete as the Privacy Policy provides. Incorrect: Data Safety does not provide that information, but the Privacy Policy mentions it. Inconsistency: Data Safety is provided but its description is inconsistent with the Privacy Policy information provided. Note: always gives me the result (0 or 1, 1 is yes, 0 is no) in the form below: {"incorrect": (0 or 1), "incomplete": (0 or 1), "inconsistent": (0 or 1)}. Please in the answer, just give me the json only and in English. Below is information for 2 parts:\nData Safety: ''' + data_safety_content + '''\nPrivacy Policy:\n''' + privacy_policy_content + ''' ''',
                },
            ]
            response = openai.ChatCompletion.create(
                model=os.getenv("MODEL_GPT_4_0"), messages=prompt_message
            )
            assistant_reply = response.choices[0].message["content"]
            return assistant_reply
        except Exception as e:
            return "Error: The prompt length exceeds the maximum allowed length of 8192 tokens."

    @staticmethod
    async def loop_csv(input_csv_path, output_csv_path):
        with open(input_csv_path, "r", newline="", encoding="utf-8") as csvfile, open(
            output_csv_path, "w", newline="", encoding="utf-8"
        ) as outputfile:

            reader = csv.reader(csvfile)
            writer = csv.writer(outputfile)

            headers = next(reader)
            writer.writerow(headers)

            for index, row in enumerate(reader):
                print(
                    "\n_____________ Run times "
                    + str(index + 1)
                    + " <"
                    + row[0]
                    + "> "
                    + "_____________"
                )
                gpt_result = HANDLER().ask_gpt(row[4], row[5])
                row[headers.index("result")] = HANDLER().remove_empty_lines(
                    gpt_result
                )
                writer.writerow(row)
                print("~~~~~~~~~~~~~~ Success ~~~~~~~~~~~~~~\n")


async def main():
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")

    input_csv_path = "scenario/case-06/data/450-train-need.csv"
    output_csv_path = "scenario/case-06/data/450-train-llm.csv"

    await HANDLER().loop_csv(input_csv_path, output_csv_path)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
