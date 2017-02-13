import os
import re

from noteboat import config


class Note:
	def __init__(self, name):
		self.name = name
		self.read_details_from_file()

	def read_details_from_file(self):
		try:
			with open(self.temp_path(), 'r', encoding='utf-8') as infile:
				self.text = infile.read()
		except IOError:
			try:
				with open(self.path(), 'r', encoding='utf-8') as infile:
					self.text = infile.read()
			except FileNotFoundError:
				self.text = "new note\nnew note\n"

		(self.title, self.desc, junk) = self.text.split('\n', 2)

	def get_title(self):
		return self.title or "[no title]"

	def get_sortable_title(self):
		sortable_title = self.get_title().lower()
		sortable_title = re.sub(r"^\W+", "", sortable_title)
		sortable_title = re.sub(r"^the ", "", sortable_title, re.IGNORECASE)
		return sortable_title

	def write(self):
		path = self.temp_path()
		os.makedirs(os.path.dirname(path), exist_ok=True)
		text_to_write = self.text.replace('\r\n', '\n') + "\n"
		with open(path, 'w', encoding='utf-8') as outfile:
			outfile.write(text_to_write)

	def path(self):
		basename = os.path.basename(self.name)
		basedir = config.note_file_base.rstrip('/')
		return "%s/%s.%s" % (basedir, basename, config.file_extension)

	def temp_path(self):
		basename = os.path.basename(self.name)
		basedir = config.saved_file_base.rstrip('/')
		return "%s/%s.%s" % (basedir, basename, config.file_extension)
