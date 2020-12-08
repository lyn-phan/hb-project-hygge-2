# Hygge 

Hygge is a full-stack web application that makes it easy and comforting to collaborate with friends when you want to plan a trip or an event.

## 🌴 Contents:
- [Features](#features)
- [Technologies & Stack](#techstack)
- [Set-up & Installation](#setup)
- [About the Developer](#about)


## <a name="features"></a> 🌴 Features:

User-friendly landing page that evokes hygge from the start
<br>
<br>
![](static/gifs/landing_page_1.gif)
<br>

User registration and log-in
<br>
<br>
![](static/gifs/sign_up.gif)
<br>

Ability to invite friends on trips
<br>
<br>
![](static/gifs/Invite_friends.gif)
<br>

Ability to add events on a shared calendar
<br>
<br>
![](static/gifs/add_to_cal.gif)
<br>


## <a name="techstack"></a> 🌴 Technologies and Stack
- Backend: Python, Flask, SQLAlchemy, PostgreSQL
- Frontend: Javascript, jQuery, Boostrap, Google Fonts, HTML, CSS
- APIs: Toast.UI


## <a name="setup"></a> 🌴 Set-up & Installation
Clone or fork repository:
```
$ git clone https://github.com/lyn-phan/hb-project-hygge-2
```
Create and activate a virtual environment:
```
$ virtualenv env
$ source env/bin/activate
```
Install dependencies:
```
$ pip3 install -r requirements.txt
```
With PostgreSQL, create the database:
```
$ createdb travel
```
Seed your database:
```
$ python3 seed_database.py
```
Run the app from the command line:
```
$ python3 server.py
```

<br>

## <a name="about"></a> 🌴 About the Developer:
Lynda graduated from UC Davis with a BS in Human Development and started working in Early Childhood programs after graduation. After learning more about 
the exciting world of tech, she broke her way in and spent the next 8 years in various Recruiting positions. where she helped build and scale 
teams at tiny startups, pre-IPO and large tech companies.  Although this work was challenging in its own way, Lynda missed learning and wanted to develop 
her problem solving skills through programming. She was also inspired by many other women in the industry who made a career change and hopes that she can 
continue working toward increasing women's representation in technical roles.
<br>

This is her first full-stack project. She can be found on [Linkedin](https://www.linkedin.com/in/lkphan/) and [Github](https://github.com/lyn-phan).