import os

from dotenv import load_dotenv

load_dotenv(os.path.join(os.getenv('NOTEBOAT_BASE_DIR'), ".env"))

homedir = os.getenv('HOME')
note_file_base = os.getenv('NOTEBOAT_NOTE_FILE_BASE', "%s/notes/" % (homedir))
saved_file_base = os.getenv('NOTEBOAT_SAVED_FILE_BASE', "%s/saved" % (note_file_base))
file_extension = os.getenv('NOTEBOAT_FILE_EXTENSION', "txt")
