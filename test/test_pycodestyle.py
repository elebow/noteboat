import os
import fnmatch
import unittest
import pycodestyle


class TestCodeFormat(unittest.TestCase):

	def test_conformance(self):
		style = pycodestyle.StyleGuide(config_file='tox.ini')
		result = style.check_files(self.find_py_files())
		self.assertEqual(result.total_errors, 0)

	def find_py_files(self):
		#return glob.iglob('noteboat/noteboat/**/*.py', recursive=True)	#for python3.6
		files = []
		for root, dirnames, filenames in os.walk('noteboat'):
			for filename in fnmatch.filter(filenames, '*.py'):
				files.append(os.path.join(root, filename))
		return files

if __name__ == '__main__':
	unittest.main()
