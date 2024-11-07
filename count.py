import asyncio
import translate
import sys
def count_characters(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()  # Read the entire file content
            char_count = len(content)  # Count the number of characters
            return char_count
    except FileNotFoundError:
        return f"The file {filename} does not exist."
    
def viet_to_eng_translations():
    with open(str(sys.argv[1]), 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    line = line.strip().lower()
                    english = asyncio.run(translate.translate_text(line))
                    english = english["data"]["translations"]
                    #print(english)
                    english = [translation["translatedText"] for translation in english]
                    english = ', '.join(english)
                    with open("testing.txt", 'a', encoding='utf-8') as f:
                        f.write(line)
                        f.write(', ')
                        f.write(english)
                        f.write('\n')
                except KeyboardInterrupt:
                    break
                except Exception as e:
                    print(e)
                    print(line)

# Example usage
filename = 'yourfile.txt'  # Replace with your file's name
viet_to_eng_translations()
#print(str(sys.argv[1]))