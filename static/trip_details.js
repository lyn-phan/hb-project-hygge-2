"use strict";

// add events to trip page
const addEvents = (event_name) => {
    $('#events_list').append(event_name);
};

// Event handlers

$('#create_event').on('click', () => {
    // addEvents('event_name');
    console.log('this works!')
});