"use strict";

function addEvents (evt) {
    evt.preventDefault();

    $.get('/trips/<trip_id>', (res) =>{
        let eventList = '';
        $('#events_list').append(`
        <label for="event_name"> Event name: </label>
        <input type="event_name" name="event_name">`)
        console.log('hi! I am here!')
    })};


$('#event-adder').on('click', addEvents);