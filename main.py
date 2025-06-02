import os
from google import genai
from dotenv import load_dotenv
from rich import print
from pydantic import BaseModel

load_dotenv()



client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain how AI works in a few words",
)

print(response.text)





class Recipe(BaseModel):
    recipe_name: str
    ingredients: list[str]


response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="List a fe popular cookie recipe, and include the amounts of ingredients.",
    config={
        "response_mime_type": "application/json",
        "response_schema": Recipe,
    },
)
# Use the response as a JSON string.
print(response.text)

# Use instantiated objects.
recipe: Recipe = response.parsed

print(recipe)