A lightweight, web-based notebook that uses text files for storage.

Background
==========

This app was written to fill a particular niche. I keep a variety of notes as text files in `~/notes/`, and I often edit them quickly as thoughts strike me while working. I find it convenient and versatile, but it doesn't leave me many good options for editing notes from, say, a smartphone with cumbersome ssh tools.

Description
===========

Noteboat is a lightweight, web-based note viewer and editor that uses my existing notes directory as storage. Because I am a little bit paranoid, notes are written to a different location to prevent accidental overwriting (but this can be configured away). The new files can then be merged with your favorite file merge tool; you can even have git repositories at one or both locations.

Noteboat was designed with a Unixy philosophy and complies with the 12-factor app philosophy as much as practical for such a tiny tool. Access control is left to the web server or WSGI middleware (I rely on a VPN for auth); backup is covered by the regular backup of my homedir; notes are stored in plain text form and easily read by humans or other tools.

Setup
=====

To configure, simply set environment variables (perhaps with the supported `.env` file) `NOTEBOAT_NOTE_FILE_BASE`, `NOTEBOAT_SAVED_FILE_BASE`, and `NOTEBOAT_FILE_EXTENSION`. The app can be run in any WSGI container.

You have a lot of flexibility in how you want to compartmentalize your notes directory. I use linux's "bind mount" facility to expose the directory to the app safely.

Usage
=====

The first two lines of every file are assumed to be the title and description, respectively. They are displayed on the index page. Behavior is undefined for files shorter than two lines.

Create new files with the form at the bottom of the index page. The text field is for the file name.

There is no way to delete files through the interface, to guard against accidental removal.
