from django.shortcuts import render
from openai import OpenAI

client = OpenAI(api_key='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')
system_prompt = "As the project manager for our software development project, I need assistance in task assignment. Below are the project details, and time constraint. Please provide task assignments for the project requirements.:"
user_prompt=""
end_prompt = "Please provide in detail each task assignment for the team member and "
final_prompt = system_prompt + user_prompt
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{
            "role": "user",
            "content": final_prompt
        }],
)


# Create your views here.
