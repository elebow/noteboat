import os
import sys

base_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, base_dir)
os.environ['NOTEBOAT_BASE_DIR'] = base_dir

activate_this = os.path.join(base_dir, 'virtualenv/bin/activate_this.py')

with open(activate_this) as file_:
	exec(file_.read(), dict(__file__=activate_this))

from noteboat import app as application
