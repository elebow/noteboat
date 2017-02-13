from mock import MagicMock
import unittest

from noteboat.note import Note

class NotesTestCase(unittest.TestCase):

	def test_get_sortable_title(self):
		Note.read_details_from_file = MagicMock()
		note = Note("my great note")

		note.title = 'aa'
		assert(note.get_sortable_title() == 'aa')

		note.title = 'Ad'
		assert(note.get_sortable_title() == 'ad')

		note.title = 'The ab'
		assert(note.get_sortable_title() == 'ab')

		note.title = 'the ac'
		assert(note.get_sortable_title() == 'ac')

		note.title = '#gb'
		assert(note.get_sortable_title() == 'gb')

		note.title = '33 ge'
		assert(note.get_sortable_title() == '33 ge')

		note.title = '  .hh'
		assert(note.get_sortable_title() == 'hh')

if __name__ == '__main__':
	unittest.main()
