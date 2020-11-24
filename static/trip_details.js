"use strict";


$('#create-event-button').on('click', () => {
    // onClick renders the form from Trip_Details
        $('#events_list').append(`
        <form>
        <label for="new-event-input"> Event name:</label>
        <input type="text" id="new-event-input"></input>
        <label for="dateTimePicker"> Date:</label>
        <input name="dateTimePicker" id="dateTimePicker"></input>
        <textarea id="event_info" name="event" placeholder="Describe event"></textarea>
        <input type="submit" name="event-name" id="submit-event">
        </form>`);
        var instance = new dtsel.DTS('input[name="dateTimePicker"]'); 
    $('#submit-event').on('click',(evt) => {
        // onClick, goes to server and grabs data from form and adds to dictionary
        evt.preventDefault();
        const formInputValue = $('#new-event-input').val();
        const formDateValue = $('#dateTimePicker').val();
        $.post('/trips/add-trip-event', {eventFormInput: formInputValue, eventDateInput: formDateValue }, (res) => {
            $('#results').append(`<li>${res.eventFormInput} | ${res.eventDateInput} </li>`);
        });
        document.getElementById("events_list").innerHTML = '';
    }
    )});

    // TODO: get the event to add in database. print to Events list rather
    // than just to the console 
 




