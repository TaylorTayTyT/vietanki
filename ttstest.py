import translate
import asyncio
import time

def find_translation(file_path, viet_word):
    with open(file_path, 'r', encoding='utf-8', errors="ignore") as file:
        for line in file:
            try:
                word, translation = line.strip().split(',', 1)
                if word == viet_word:
                    return translation
            except Exception as e:
                print(line.strip().split(','))
                print(e)
                
            
    return None

# Example usage
#print(find_translation("testing.txt", "chào"))
english = asyncio.run(translate.translate_text("sống để bụng chết mang theo"))
english = english["data"]["translations"]
english = [translation["translatedText"] for translation in english]
print(english)
