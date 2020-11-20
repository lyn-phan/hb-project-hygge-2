"use strict";

$('#add-event-button').on('click', () => {
    // let eventList = '';
        $('#events_list').append(`
        <form>
        <label for="event_name"> Event name: </label>
        <input type="text" id="new-event-input"> </input>
        <input type="submit" name="event_name" id="submit-event">
        </form>`);
    $('#submit-event').on('click',(evt) => {
        evt.preventDefault();
        $.post('/trips/add-trip-event', {eventFormInput: 'new_event_to_add'}, (res) => {
            $('#events_list').append($('new_event_to_add'))
            alert('hi! this works!')
            console.log(res)
        })}
    )});
            // eventFormInput --> where form input will go
            // grab with request.form.get in server