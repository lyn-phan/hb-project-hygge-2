"use strict";

$('#create-event-button').on('click', () => {
    // onClick renders the form from Trip_Details
        $('#events_list').append(`
        <form>
        <label for="event_name"> Event name: </label>
        <input type="text" id="new-event-input"></input>
        <textarea id="event_info" name="event" placeholder="Describe event"></textarea>
        <input type="submit" name="event-name" id="submit-event">
        </form>`);
    $('#submit-event').on('click',(evt) => {
        // onClick, goes to server and grabs data from form and adds to dictionary
        evt.preventDefault();
        const formInputValue = $('#new-event-input').val();
        $.post('/trips/add-trip-event', {eventFormInput: formInputValue}, (res) => {
            $('#events_list').append(`<div>${res}</div>`)
            console.log("input[name='event-name']")
        })}
    )});
