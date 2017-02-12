import os

from noteboat import config
from noteboat.note import Note


class Notes:
	def __init__(self):
		self.notes = {}
		self.load_note_names()

	def note_names(self):
		return sorted(self.notes, key=lambda x: self.notes[x].get_sortable_title())

	def load_note_names(self):
		filtered_names = self._filtered_names()
		for name_with_extension in filtered_names:
			extension_length = len(config.file_extension)
			name = name_with_extension[0:-(extension_length + 1)]
			self.notes[name] = Note(name)

	def _filtered_names(self):
		names = os.listdir(config.note_file_base)
		names += os.listdir(config.saved_file_base)
		return list(filter(lambda x: x.endswith(config.file_extension), names))

	def __getitem__(self, key):
		if key not in self.notes.keys():
			self.notes[key] = Note(key)
		return self.notes[key]
