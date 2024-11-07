from aqt import mw, gui_hooks
from aqt.qt import *
from aqt.utils import showInfo
import os
import sys
import asyncio
sys.path.append(os.path.join(os.getenv('APPDATA'), 'Anki2', 'addons21', 'viet_dict'))
# Add the path to the src directory to sys.path
sys.path.append(os.path.join(os.getenv('APPDATA'), 'Anki2', 'addons21', 'viet_dict', 'libs'))

# Now import load_dotenv from the dotenv package
import dotenv
import aiohttp
dotenv.load_dotenv()
from translate import translate_text

note_type_name = "Sample"
print(os.path.abspath(os.getcwd()))

def start() -> None:
    if mw.col.models.by_name(note_type_name):
        return
    new_model = mw.col.models.new(note_type_name)
    
    fields = ["Viet", "English", "Sentence", "Sound"]
    for i, field_name in enumerate(fields):
        field = mw.col.models.newField(field_name)
        field.ord = i
        field.font = "Arial"
        field.size = 20
        mw.col.models.addField(new_model, field)
    
    template = mw.col.models.newTemplate("Sample Template")
    template.qfmt = "<div>{{Viet}}</div>"
    template.afmt = "<div>{{Viet}}</div><div>{{English}}</div><div>{{Sentence}}</div><!-- {{Sound}}-->"
    
    mw.col.models.addTemplate(new_model, template)
    mw.col.models.add(new_model)

gui_hooks.profile_did_open.append(start)

def on_add_cards_init(addcard):
    label1 = QLabel("Hello")
    label2 = QLabel("World")
    
    addcard.form.verticalLayout_3.addWidget(label1)
    addcard.form.verticalLayout_3.addWidget(label2)
    
    def get_field_values():
        field_values = {}

        # Check if `editor` and `note` are available in `addcard`
        if hasattr(addcard, 'editor') and hasattr(addcard.editor, 'note'):
            note = addcard.editor.note

            # Loop through all fields in the note and get the text
            for field_name, field_text in zip(note.keys(), note.fields):
                field_values[field_name] = field_text

        # Show field values for testing purposes
        return field_values

    # Add a button to trigger the value retrieval (for testing purposes)
    retrieve_button = QPushButton("Get Field Values")
    retrieve_button.clicked.connect(get_field_values)
    addcard.form.verticalLayout_3.addWidget(retrieve_button)
    
    def eventFilter(self, source, event):
        #print(event.type())
        if event.type() == QEvent.Type.KeyRelease and event.key() == Qt.Key.Key_Tab:
            
            #go to media directory
            head, _ = os.path.split(os.getcwd())
            parent_dir, _ = os.path.split(head)
            media = os.path.join(parent_dir, os.getenv("USER"), "collection.media")
            viet = get_field_values()['Viet']
            if viet:
                note = addcard.editor.note
                english = asyncio.run(translate_text(viet))
                english = english["data"]["translations"]
                print(english)
                english = [translation["translatedText"] for translation in english]
                note.fields[1] = '\n'.join(english)
                
                #assign the audio
                audio_file = f"{viet}.mp3"
                audio_path = os.path.join(media, audio_file)
                note.fields[3] = f'{{{{audio:{audio_file}}}}}'
                addcard.editor.loadNote()
            showInfo("Tab was pressed")
            return True  # Mark event as handled
        return False  # Pass event to other handlers
    
    addcard.form.centralwidget.installEventFilter(addcard)
    addcard.eventFilter = eventFilter.__get__(addcard)

print(media)
gui_hooks.add_cards_did_init.append(on_add_cards_init)
