import asyncio
import multiprocessing
import translate
import os
import time

# Asynchronous function for processing a line
async def process_line(line, counter, lock):
    line = line.strip()
    if(os.path.exists(line + ".mp3")):
        return
    try:
        await translate.tts(line)
    except Exception as e:
        print(f"Error processing line: {line}, error: {e}")

# Synchronous wrapper for the async function
def process_line_sync(line, counter, lock):
    with lock:
        counter.value += 1
        if(counter.value % 900 == 0):
            print("sleep")
            time.sleep(60)
    asyncio.run(process_line(line, counter, lock))

def generate_audio_parallel():
    # Read lines from the file
    with open("Viet74K.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    with multiprocessing.Manager() as manager:
        counter = manager.Value("i", 1)
        lock = manager.Lock()
        # Create a pool with the maximum number of available cores
        with multiprocessing.Pool(10) as pool:
            # Map the synchronous wrapper function to each line
            pool.starmap(process_line_sync, [(line, counter, lock) for line in lines])

# Run the parallel processing function
if __name__ == "__main__":
    generate_audio_parallel()
