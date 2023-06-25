
# Project Title

QuantifiedSelf App - Quantified Self app is a self-tracking app 
    used for tracking various activities of User. Users can specify
    the type of tracker they want to make and log their activities
    accordingly. Many modern-day applications are built on top of
    this. For e.g. – Smart Watches track your running and calories
    count and you make your progress accordingly.

[view this project live](https://quantifiedself-app.kumargaurav10.repl.co/login?next=%2F)

## Frameworks used

- Flask for application code

- Jinja2 templates + Bootstrap for HTML generation and styling

- SQLite for data storage

- All demos should be possible on a standalone platform like replit.com and should not require setting up new servers for database and frontend management

## Features

- Used for self tracking - tracking habits, activities, other life parameters etc.

- User can have multiple trackers
- Each tracker will have a 
    - ID Name
    - Description
    - tracker
    - type
    - settings
- User can log to one more tracker at any time, each time it’s logged it will capture
    - Timestamp
    - tracker
    - Value
    - Notes
- System will track progress over time and shows graphs trend lines etc

    ## Terminology

    - Tracker - Corresponding to the 
    - TrackerType - Type says what data is captured
       - Numerical 
       - Multiple Choice
       - Time Duration
       - Boolean
    - Logging - Logging an event to a tracker by providing values
    - Trendline - Shows the list of logged events and may be graphs

## Related

Here are some related references

[Quantified Self](https://en.wikipedia.org/wiki/Quantified_self)

## Codebase hierarchy

├───app.py (main app.py) file to be called to start server for web app

├───requirements.txt - File of pip install statements for your app

├───myprojectApp (main project folder), sub-components will be in separate folders

    │   │   data.sqlite
    │   │   models.py
    │   │   __init__.py
    │   │   views.py
    |   |   auth.py
    │   │   templates folder
    │   │              login.html
    |   |              sign_up.html
    |   |               about.html
    |   |               base.html
    |   |                home.html
    |   |               profile_page.html
    |   |               add log page, edit log page (HTML)
    |   |               add tracker, edit tracker (HTML)
    │   | ───static (Where you store your CSS, JS, Images, Fonts, etc...)

# Hi, I'm Gaurav! 👋


## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kumar-gaurav-a1a774198/)

