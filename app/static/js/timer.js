function cursorDeactivationTimer(toggle) {
    if (toggle){
        var timeInput = document.getElementById('customTime')
        var [selectedHour, selectedMinute] = timeInput.value.split(":").map(Number)

        var currentTime = new Date()
        var [currentHour, currentMinute] = [currentTime.getHours(), currentTime.getMinutes()]

        var timeDifference = (selectedHour * 60 + selectedMinute) - (currentHour * 60 + currentMinute)

        console.log(timeDifference)

        cursorTimer = setTimeout(() => activateCursor(false), timeDifference * 60 * 1000)
    } else {
        clearTimeout(cursorTimer)
    }
}

function handleCheckbox() {
    var checkbox = document.getElementById('timerCheckbox')
    if (checkbox.checked) {
        cursorDeactivationTimer(true)
    } else {
        cursorDeactivationTimer(false)
    }
}
