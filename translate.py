import asyncio
import aiohttp
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

async def translate_text(input):
    url = "https://translation.googleapis.com/language/translate/v2?key=" + os.getenv("API")
    headers = {"Content-Type": "application/json"}
    
    # Fetch API key from environment variables
    api_key = os.getenv("API")
    print(api_key)
    if not api_key:
        print("API key not found")
        return

    query = {
        "q": input,
        "target": "en",
        "format": "text",
        "source": "vi",
        "model": "base",
    }
    
    # Asynchronous request using aiohttp
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=query, headers=headers) as response:
            if response.status == 200:
                result = await response.json()
                print(result)
            else:
                print(f"Error: {response.status}")
                print(await response.text())

# Run the async function
asyncio.run(translate_text("chao"))
