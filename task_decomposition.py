import os
import re
import json
from openai import OpenAI
from tqdm import tqdm
import argparse


def query_pivotal_llm_for_multi_turn(client, messages, model_name="gpt-3.5-turbo", temperature=0.0, top_p=1.0, max_tokens=256, seed=1126):

    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model_name,
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens,
        seed=seed
    )

    return chat_completion.choices[0].message.content


def task_decomposition_prompt_template():

    system_prompt = "You are an expert on speech domain and good at coding."

    user_prompt_1 = f'''
You are given the following task instructions, where each instruction may require you to do a speech processing task.
While the required tasks are diverse, they may have some common sub-tasks.
For examples, automatic speech recognition may be helpful for several tasks.
Another example is that some tasks are sound classification tasks, and these tasks may be solved using a single module.
Now, I want you to analyze the instructions, identify the corresponding speech processing tasks, and solve the tasks in the instructions by writing the Python code for each task.
In your code, you should modularize the sub-tasks as a code module, e.g. speech_recognition(audio), query_LLM(prompt), etc.
Then you should finish the tasks by calling the code modules of sub-tasks. 
However, as you don't have the official module list, you can create modules when you need. The constraint is that you should reuse the modules as much as possible. And make the size of th module list as small as possible.
This means that if two different tasks require the same sub-task, you should use the same module to finish the sub-task instead of creating a similar one again.
Please keep in mind that you don't need to implement the modules, just define them with a placeholder like speech_recognition(audio), and we will complete the implementation for you.
Besides, here is a module named query_LLM(prompt) that can be used to query the language model for extracting information with proper prompt. You should make use of this module and reduce the number of modules you create.
If the task can be correctly solved by using automatic speech recognition and query LLM, you should use these two modules to finish the task instead of creating a new one.
However, the query_llm module is not omnipotent. It cannot have the audio information, and the speech recognition will only transcribe the speech into text, and some audio information like noise level, or speaker information will be lost during the transcription.
Hence, if the task require audio information beyond the transcription, you should use other modules.

Here is an example:
Suppose you are given the following instruction: Give me the transcription of the following audio file.
This will require you to do automatic speech recognition. You can write a module called speech_recognition(audio) to finish this task.
The final output should have the format like this:
`````python`````
# Code for instruction 1
# Task needed: automatic speech recognition
def execute_command(audio):
    transcription = speech_recognition(audio)
    return transcription

# Code for instruction 2
# Task needed: sound classification
def execute_command(audio):
    sound_class = sound_classification(audio)
    return sound_class
````````````````
If multiple instructions are provided, you should write the code for each instruction separately and index them in the final output.
Now given the following task instruction, please write the Python code to solve the tasks. The output should follow the format above.
Instruction: 
'''
    return system_prompt, user_prompt_1

# Part1: Task Decomposition.
# Provide your own task instructions in the below list.
instruction_list = [...]

system_prompt, user_prompt_1 = task_decomposition_prompt_template()

for i in range(len(instruction_list)):
    user_prompt_1 += f"Instruction {i+1}: {instruction_list[i]}\n"

print(user_prompt_1)

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt_1}
]

openai_api_key = "YOUR_OPENAI_API_KEY"
client = OpenAI(api_key=openai_api_key)

results = query_pivotal_llm_for_multi_turn(client, messages, model_name="gpt-4o", temperature=0.0, top_p=1.0, max_tokens=4096)
print(results)
with open('task_decomposition.txt', 'w') as f:
    f.write(results)


# Part2: Deduplicate the used modules.
prompt_for_summarize = f'''
Given the following code:
{results}

Please count and summarize the used modules for me. The format should be:
1. speech_recognition: the number of usage of speech_recognition
2. query_LLM: the number of usage of query_LLM
...

Don't generate code. Just summarize the used modules.
'''


message_for_summarize= [
    {"role": "user", "content": prompt_for_summarize}
]

summarize_for_first_correction = query_pivotal_llm_for_multi_turn(client, message_for_summarize, model_name="gpt-4o", temperature=0.0, top_p=1.0, max_tokens=4096)
print(summarize_for_first_correction)
with open('deduplicate_task_decomposition.txt', 'w') as f:
    f.write(summarize_for_first_correction)