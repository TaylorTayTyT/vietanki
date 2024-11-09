import asyncio
import os
from decode_audio import decode_tts_output
import json
import sys
sys.path.append(os.path.join(os.getenv('APPDATA'), 'Anki2', 'addons21', 'viet_dict'))
import aiohttp
import dotenv
from base64 import decodebytes
dotenv.load_dotenv()

async def translate_text(input):
    url = "https://translation.googleapis.com/language/translate/v2?key=" + os.getenv("API")
    headers = {"Content-Type": "application/json"}
    
    # Fetch API key from environment variables
    api_key = os.getenv("API")
    #print(api_key)
    if not api_key:
        #print("API key not found")
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
                #print(result)
                return result
            else:
                print(f"Error: {response.status}")
                print(await response.text())
                return None

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
                result = result["audioContent"]
                input_file_txt = os.path.join(os.getcwd(), "audio", f"{input}.txt")
                output_file_mp3 = os.path.join(os.getcwd(), "audio", f"{input}.mp3")
                with open(output_file_mp3, "wb") as new_file:
                    new_file.write(decodebytes(result.encode('utf-8')))
            else:
                print(f"Error: {response.status}")
                print(await response.text())

# Run the async function
#asyncio.run(translate_text("chưa"))
#asyncio.run(tts("chao"))