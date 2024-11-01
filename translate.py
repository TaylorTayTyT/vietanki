import asyncio
import aiohttp
import os
from dotenv import load_dotenv
from decode_audio import decode_tts_output
import json

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

async def tts(input):
    api_key = os.getenv("API")
    if not api_key:
        print("API key not found")
        return
    url = "https://texttospeech.googleapis.com/v1/text:synthesize?key=" + os.getenv("API")
    headers = {"Content-Type": "application/json"}
    query = {
        "input": {"text": input},
        "voice": {
            "languageCode": "vi",
            "ssmlGender": "MALE",
        },
        "audioConfig": {
            "audioEncoding": "MP3",
        },
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=query, headers=headers) as response:
            if response.status == 200:
                result = await response.json()
                with open("output.txt", "w") as f:
                    f.write(json.dumps(result))
                    decode_tts_output("output.txt", "output-audio.mp3")
                
            else:
                print(f"Error: {response.status}")
                print(await response.text())

# Run the async function
#asyncio.run(translate_text("chao"))
asyncio.run(tts("chao"))