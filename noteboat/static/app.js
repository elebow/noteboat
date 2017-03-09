window.addEventListener("beforeunload", function (event) {
	saveScrollPosition();
});

window.addEventListener("load", function (event) {
	restoreScrollPosition();
});

function saveScrollPosition() {
	var elem;
	if (editMode() === 'edit') {
		elem = document.getElementById('note_text');
	} else {
		elem = document.body;
	}

	pos = elem.scrollTop / elem.scrollHeight;
	Cookies.set(cookieKey(), pos);
}

function restoreScrollPosition() {
	pos = Cookies.get(cookieKey());
	scrollToPosition(pos);
}

function scrollToPosition(pos) {
	if (editMode() === 'edit') {
		textarea = document.getElementById('note_text');
		absPos = pos * textarea.scrollHeight;
		textarea.scrollTop = absPos;
	} else {
		absPos = pos * document.body.scrollHeight;
		window.scrollTo(0, absPos);
	}
}

function editMode() {
	return window.location.pathname.split('/')[1]
}

function cookieKey() {
	return 'scroll_' + window.location.pathname.split('/')[2];
}
