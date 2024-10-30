# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo, qconnect
# import all of the Qt GUI library
from aqt.qt import *
from aqt import gui_hooks
from anki import hooks
from anki.stdmodels import models
from anki import collection as col
from . import basic
import os
from aqt.utils import showInfo
#from keyboard import _keyboard_event

# We're going to add a menu item below. First we want to create a function to
# be called when the menu item is activated.

note_type_name = "Sample"

def add_models():
    models.append(('Viet (test)', basic.add_model))
    
def tab_press() -> None:
    if(keyboard.is_pressed('tab')):
        print("tab")

def start() -> None:
    
    """
    Show a message box with the number of cards in the current collection.

    This function is called when the menu item created below is activated.
    """
    # get the number of cards in the current collection, which is stored in
    # the main window
    """
    model = mw.col.models.by_name("Cloze")
    new_note = mw.col.newNote(model)
    new_note["Back"] = "example description"
    new_note["Front"] = "example name"
    
    
    deckId = mw.col.decks.id_for_name("TST")
    mw.col.add_note(new_note, deckId)
    """
    if(mw.col.models.by_name(note_type_name)):
        return
    new_model = mw.col.models.new(note_type_name)
    
    fld1 = {
            "name": "Viet", #name of the field
            "ord": 0, #order
            "sticky": False,
            "rtl": False,
            "font": "Arial",
            "size": 20,
            "description": "",
            "plainText": False,
            "collapsed": False,
            "excludeFromSearch": False,
            "id": None,
            "tag": None,
            "preventDeletion": False,
        }
    
    fld2 = {
            "name": "English",
            "ord": 1,
            "sticky": False,
            "rtl": False,
            "font": "Arial",
            "size": 20,
            "description": "",
            "plainText": False,
            "collapsed": False,
            "excludeFromSearch": False,
            "id": None,
            "tag": None,
            "preventDeletion": False,
        }
    fld3 = {
        "name": "Sentence",
        "ord": 2,
        "sticky": False,
        "rtl": False,
        "font": "Arial",
        "size": 20,
        "description": "",
        "plainText": False,
        "collapsed": False,
        "excludeFromSearch": False,
        "id": None,
        "tag": None,
        "preventDeletion": False,
    }
    
    fld4 = {
        "name": "Sound",
        "ord": 3,
        "sticky": False,            
        "rtl": False,
        "font": "Arial",
        "size": 20,
        "description": "",
        "plainText": False,
        "collapsed": False,
        "excludeFromSearch": False,
        "id": None,
        "tag": None,            
        "preventDeletion": False,}
    
    
    mw.col.models.add_field(new_model, fld1)
    mw.col.models.add_field(new_model, fld2)
    mw.col.models.add_field(new_model, fld3)
    mw.col.models.add_field(new_model, fld4)
    template = mw.col.models.new_template("Sample Template")
    template["qfmt"] = "<div>{{Viet}}</div>"
    template["afmt"] = "<div>{{Viet}}</div><div>{{English}}</div><div>{{Sentence}}</div>"
    print(template)
    mw.col.models.add_template(new_model, template)
    
    mw.col.models.add(new_model)
    
    #1 template required error
    print(template)
    print(new_model)
    
# set it to call testFunction when it's clicked
gui_hooks.profile_did_open.append(start)

def event(event):
    if event.type() == QEvent.KeyPress:
        ke = QKeyEvent(event)
        if ke.key() == Qt.Key_Tab:
            # special tab handling here
            return True
    return QWidget.event(event)

# Define your custom function that will run when the hook is triggered
def on_add_cards_init(addcard):
    # Add your custom behavior here
    showInfo("Add your custom behavior here")
    
    label = QLabel("hello")
    addcard.form.horizontalLayout.addWidget(label)
    print(addcard.form.setupUi)
    print(dir(addcard.form))
    # You can access the addcards object here to modify the dialog
    
    

# Append your function to the "add_cards_did_init" hook
#hooks.addHook("add_cards_did_init", on_add_cards_init)
gui_hooks.add_cards_did_init.append(on_add_cards_init)