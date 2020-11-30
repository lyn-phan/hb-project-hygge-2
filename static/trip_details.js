"use strict";


$('.create-event-button').on('click', (evt) => {
    // onClick renders the form from Trip_Details
    const idOfTrip = ($(evt.target)[0].id)
    console.log(idOfTrip);
        $('#events_list').append(`
        <form>
        <label for="newEventName"> Event name:</label>
        <input type="text" id="newEventName"></input>
        <label for="dateTimePicker"> Date:</label>
        <input name="dateTimePicker" id="dateTimePicker"></input>
        <textarea id="eventDescription" name="eventDescription" placeholder="Describe event"></textarea>
        <input type="submit" id=${idOfTrip} name="eventDetails" class ="submit-event">
        </form>`);
        var instance = new dtsel.DTS('input[name="dateTimePicker"]', 
        {dateFormat: "YYYY-MM-DD",
        timeFormat: "Thh:mmTZD" 
    });
    $('.submit-event').on('click', (evt) => {
        // onClick, goes to server and grabs data from form and adds to dictionary
        evt.preventDefault();
        const idOfTrip = ($(evt.target)[0].id);
        console.log(idOfTrip);
        console.log(evt);
        const formInputValue = $('#newEventName').val();
        const formDateValue = $('#dateTimePicker').val();
        const formDescriptionValue = $('#eventDescription').val();
        $.post(`/trips/${idOfTrip}/add-trip-event`, {'eventFormInput': formInputValue, 'eventDateInput': formDateValue, 'eventDescriptionInput': formDescriptionValue}, (res) => {
            $('#results').append(`<li>${res.new_event_name} | ${res.new_event_date} </li>`);
            console.log(res);
        });
        document.getElementById("events_list").innerHTML = '';
    })
    });

$('.add-to-cal').on('click', (evt) => {
    // onClick - grab evenut input and add to cal
    evt.preventDefault();
    const formInputValue = $('#newEventName').val();
    const idOfTrip = ($(evt.target)[0].id);
    $.post(`/trips/${idOfTrip}/add-trip-event`, {'eventFormInput': formInputValue, 'eventDateInput': formDateValue}, (res) => {
        $('#results').append(`<li>${res.new_event_name}</li>`);
        console.log(res);
    });
});

//     // document.getElementById("events_list").innerHTML = '';
//     });
// call cal create


