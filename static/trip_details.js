"use strict";

$('#event-adder').on('click', () => {
    let eventList = '';
        $('#events_list').append(`
        <form>
        <label for="event_name"> Event name: </label>
        <input type="text" id="new-event-on-vacation"> </input>
        <input type="submit" name="event_name" id="submit-event">
        </form>`);
    $('#submit-event').on('click',(evt) => {
        evt.preventDefault();
        // console.log($('#new-event-on-vacation').value)
        $.post('/trips/add-trip-event', {eventData: 'yay!'}, (res) =>{
            // eventData --> where form input will go
            // grab with request.form.get in server
            alert('hi! this works!')
            console.log(res)
        })}
    )});



// function addEvents (evt) {
//     evt.preventDefault();

//     $.get('/trips/<trip_id>', (res) =>{
//         let eventList = '';
//         $('#events_list').append(`
//         <li>
//         <label for="event_name"> Event name: </label>
//         <input type="event_name" name="event_name">
//         </li>);
//         console.log('hi! I am here!');
//     })};

//     $('#event-adder').on('click', addEvents);