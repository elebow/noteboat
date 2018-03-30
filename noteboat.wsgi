import os
import subprocess
import sys

# Python3 CLI apps (especially those using click) really like these to be set
if not 'LC_ALL' in os.environ:
	os.environ['LC_ALL'] = 'C.UTF-8'
if not 'LANG' in os.environ:
	os.environ['LANG'] = 'C.UTF-8'

base_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, base_dir)
os.chdir(base_dir)

os.environ['NOTEBOAT_BASE_DIR'] = base_dir

venv_dir = subprocess.Popen(["pipenv", "--venv"], stdout=subprocess.PIPE).stdout.read().rstrip()
activate_this = os.path.join(venv_dir, b'bin/activate_this.py').decode('utf-8')

with open(activate_this) as file_:
	exec(file_.read(), dict(__file__=activate_this))

from noteboat.noteboat import app as application
