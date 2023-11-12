function activateCursor(toggle) {
    fetch("/start", {
        method: "POST",
        body: JSON.stringify({toggle: toggle})
        }).then((_resp) => {
            window.location.href = "/";
    })
}

var cursorActive = false;

function toggleCursorButton() {
    var button = document.getElementById('cursorButton')
    cursorActive = !cursorActive

    if (cursorActive) {
        button.innerHTML = 'Stop (or press Space)';
    }
    activateCursor(cursorActive)
}

document.addEventListener('keydown', (e) => {
    if (e.key === ' ') {
    toggleCursorButton()
    }
})
