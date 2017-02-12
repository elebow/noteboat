from flask import Flask, redirect, render_template, request, url_for
import os
import os.path

from noteboat.notes import Notes

app = Flask(__name__)
# app.debug = True

notes = Notes()


@app.route('/')
def notes_index():
	notes.load_note_names()
	notes_info = [{
		'name': name,
		'title': notes[name].get_title(),
		'desc': notes[name].desc}
		for name in notes.note_names()]
	return render_template('note_index.html', notes_info=notes_info)


@app.route('/show/<string:name>')
def note_show(name):
	notes[name].read_details_from_file(),
	args = {
		'note_name': name,
		'note_text': notes[name].text,
		'readonly': True
	}
	return render_template('note_show.html', **args)


@app.route('/edit/<string:name>')
def note_edit(name):
	args = {
		'note_name': name,
		'note_text': notes[name].text,
		'readonly': False
	}
	return render_template('note_edit.html', **args)


@app.route('/create')
def note_create():
	args = {
		'note_name': request.args['note_name'],
		'note_text': "",
		'readonly': False
	}
	return render_template('note_edit.html', **args)


@app.route('/write/<string:name>', methods=['POST'])		# TODO should be PUT
def note_write(name):
	text = request.form['note_text'].rstrip()
	notes[name].text = text
	notes[name].write()

	return redirect(url_for('note_show', name=name))
