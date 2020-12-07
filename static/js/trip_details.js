"use strict";

// onClick - renders form to add a friend to the trip
$('.invite-friends-along').on('click', (evt) => {
    const idOfTrip = ($(evt.target)[0].id);

    document.querySelector("#form-holder").innerHTML = `
        <form>
        <br>
        <label for="friend-fname">First name: </label> 
        <input type="text" id="friend-fname"></input>
        <br> 
        <label for="friend-lname">Last name: </label> 
        <input type="text" id="friend-lname"></input>
        <br>  
        <label for="friend-email">Email: </label> 
        <input type="text" id="friend-email"></input> 
        <br>
        <input type="submit" id=${idOfTrip} class="submit-friends">
        </form>
        <br>`;

    $('.submit-friends').on('click', (evt) => {
        evt.preventDefault();
        const idOfTrip = ($(evt.target)[0].id);
        console.log(idOfTrip)
        const formInputFname = $('#friend-fname').val();
        const formInputLname = $('#friend-lname').val();
        const formInputEmail = $('#friend-email').val();
        $.post(`/trips/${idOfTrip}`, {'friendFirstName': formInputFname, 'friendLastName': formInputLname, 'friendEmail': formInputEmail},
         (res) => {
             document.querySelector("#form-holder").innerHTML = '';
            alert(`${res.friend_first} is coming on the trip!`);
            $('#attendees-results').append(`<li>${res.friend_first}</li>`);
         }
        )
    }
    )
}
);

$('.create-event-button').on('click', (evt) => {
    // onClick renders the form from Trip_Details
    const idOfTrip = ($(evt.target)[0].id);
    document.querySelector("#results").innerHTML = `
        <form>
        <label for="newEventName"> Event name:</label>
        <input type="text" id="newEventName"></input>
        <br>
        <label for="dateTimePicker"> Date:</label>
        <input name="dateTimePicker" id="dateTimePicker"></input>
        <br>
        <textarea id="eventDescription" name="eventDescription" placeholder="Describe event"></textarea>
        <input type="submit" id=${idOfTrip} name="eventDetails" class ="submit-event">
        </form>`;

        var instance = new dtsel.DTS('input[name="dateTimePicker"]', 
        {dateFormat: "YYYY-MM-DD",
        timeFormat: "Thh:mmTZD"
    });
    $('.submit-event').on('click', (evt) => {
        // onClick, goes to server and grabs data from form and adds to dictionary
        evt.preventDefault();
        const idOfTrip = ($(evt.target)[0].id);
        const formInputValue = $('#newEventName').val();
        const formDateValue = $('#dateTimePicker').val();
        const formDescriptionValue = $('#eventDescription').val();
        $.post(`/trips/${idOfTrip}/add-trip-event`, {'eventFormInput': formInputValue, 'eventDateInput': formDateValue, 'eventDescriptionInput': formDescriptionValue}, 
        (res) => {
            $('#results').append(`<li>${res.new_event_name} | ${res.new_event_date} </li>`);
        const options = {
            title: res.new_event_name,
            start: res.new_event_date
            };
            createCalendarEvent(options)
        });
        document.getElementById("events_list").innerHTML = '';
   }
  )
 }
);