var modal = document.getElementById('modal');
var span = document.getElementById('closeBtn')[0];

/**Custom message modal stuff
 * Currently unused but may use later
 */
function custAlert(title, message) {
    document.getElementById('modal_title').innerHTML = title;
    document.getElementById('modal_message').innerHTML = message;
    modal.style.display = "block";
}

span.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

//Checks the input of the feed schedule form for valid input
function check_input() {
    var feedStart = document.getElementById('feedStart').value;
    var feedInterval = document.getElementById('feedInterval').value;

    //Input needs to exist
    if (feedStart == "" || feedInterval == "") {
        alert('Please fill in all fields!');
        return false;
    }
    /**An interval less than 1 would run continuously
     * For practical purpose there would be no reason to need feed intervals less than 1 hour
     */
    else if (feedInterval < 1) {
        alert('Please enter a non-negative feed interval!');
        return false;
    }
    else {
        alert('You successfully changed the feed schedule!');
        return true;
    }
}

//Ultimately decided against using this, but may use it in the future
function resetController() {
    alert('You successfully reset the feeder!');
    return true;
}
