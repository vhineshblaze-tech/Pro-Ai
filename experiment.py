import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url=httpsopenrouter.aiapiv1,
    api_key=os.getenv(OPENAI_API_KEY),
)

def run_test(prompt, system_prompt=You are a helpful assistant., temperature=0.7, max_tokens=100)
    response = client.chat.completions.create(
        model=openrouterfree,
        messages=[
            {role system, content system_prompt},
            {role user, content prompt}
        ],
        temperature=temperature,
        max_tokens=max_tokens
    )
    return response.choices[0].message.content

prompt = Explain quantum computing in one simple sentence.

print(=== TEST 1 Low Temperature (0.0 - FactualDeterministic) ===)
print(run_test(prompt, temperature=0.0))

print(n=== TEST 2 High Temperature (1.0 - CreativeRandom) ===)
print(run_test(prompt, temperature=1.0))

print(n=== TEST 3 System Message (Pirate Persona) ===)
print(run_test(prompt, system_prompt=You are a pirate captain., temperature=0.7))