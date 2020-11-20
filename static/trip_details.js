"use strict";

$('#add-event-button').on('click', () => {
    // onClick renders the form from Trip_Details
        $('#events_list').append(`
        <form>
        <label for="event_name"> Event name: </label>
        <input type="text" id="new-event-input"> </input>
        <input type="submit" name="event_name" id="submit-event">
        </form>`);
    $('#submit-event').on('click',(evt) => {
        // onClick, goes to server and grabs data from form and adds to dictionary
        evt.preventDefault();
        $.post('/trips/add-trip-event', {eventFormInput: $("input[name='event_name']").val()}, (res) => {
            $('#events_list').append(`<div>${res}</div>`)
            alert('hi! this works!')
            console.log($("input[name='event_name']").val())
        })}
    )});
            // eventFormInput --> where form input will go
            // grab with request.form.get in server

    //         //         evt.preventDefault();
    //     $.post('/trips/add-trip-event', {eventFormInput: 'new_event_to_add'}, (res) => {
    //         $('#events_list').append(`<div>${res}</div>`)
    //         alert('hi! this works!')
    //         console.log($('new_event_to_add'))
    //     })}
    // )});