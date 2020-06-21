# Miguel Camacho Stream Three Project: 
# Data-Centric Development Milestone Project - Code Institute 

MileStone 3 Full Stack Software Development Course at Code Institute. Visit [gitRepo](https://github.com/MACmidiDEV/CInst-M3-Data-Centric-Development/commits/master) for entire build information. The main focus of this project was to create, develop and deploy a mongoDB database connected web application hosted on [Heroku](https://little-links-learning.herokuapp.com/) Little Links Learning is a application parents can utilize free of charge and not only have access to a collection of Learning Links but given full CRUD functionality as a contributor.

## Purpose of This Project
This website will hold a collection of learning videos geared towards toddler learning. In response to COVID-19 a VideoChat service was implemented users can now start a live learning session or join it if one has already been started.

### Strategy
My goal in the design was to make it as easy as possible to access all information on the site while striving to keep the page with collected videos simple enough to be managed by a toddler.

### Scope
With COVID-19 we have to find use of all this new time and still engage our children. Link Learning is a great way to begin to accomplish this task.

## Demo | Deploy
This site is hosted using GitHub, deployed directly from the master branch to Heroku.
The current site in production is hosted via [HEROKU](https://little-links-learning.herokuapp.com)
The GitRepo can be found on [GitHub](https://github.com/MACmidiDEV/CInst-M3-Interactive-Development)

## Wireframes
- ![LittleLinks-DRAFT](https://raw.githubusercontent.com/MACmidiDEV/CInst-M3-Data-Centric-Development/master/LittleLinks/static/images/aDRAFT.jpg "Wireframe")

## Utilized Technologies
### Languages
- HTML5
- CSS3 
- JavaScript
- Jquery
- Python3

### Frameworks & Technologies
- Materialize: For responsive web designing 
- Flask: HTML templating & routing
- Git: version control
- VSCode: code editor
- Github: hosts the website
- Jinja2: Python web template engine

### Database
- MongoDB: To store information into a database

## Environment and Configuration Variables
#### Local Variables
local env.py holds config vars 'SECRET_KEY', 'MONGO_URI' and 'DEVELOPMENT', which have the values that are required in the app.py file for the mongo URI password, the secret key password and the debug value.

#### Heroku Configuration Variables
heroku config vars 'IP', 'PORT', 'SECRET_KEY', 'MONGO_URI' and 'DEVELOPMENT' variables. The 'SECRET_KEY' and 'MONGO_URI' contain the same passwords on Heroku as they do locally in the env.py file. The 'DEVELOPMENT' variable is set to 1 during build and 0 in production

## Deployments and Installations
### Start A Virtual Environment & Install
- `python3 -m venv venv`
- `source venv/bin/activate`
- `pip3 install -r requirements.txt`
for security purposes you will need your own database connection string to [mongoDB](https://docs.mongodb.com/manual/reference/connection-string/)

## UX
### User stories
As a parent of a toddler I can skip the search and tedious task of content management and make use of Little Links to find categories of learning videos.
COVID-19 distance learning for toddlers. Start a live video session to engage your nieces and nephews.

### Surface
Some default component color schemes were combined with bold crayon like colors to ensue user conformability throughout the site 
and maintain a approachable environment for kids to interact with.

## Features
- LearningLinks: Users can add multiple LearningLinks, each LearningLink contains the Category, youTube video and a mentored message.
- Home page: Landing page informational, everything about the site. SideNav and floating button provide all navigational links available on all pages of the site.
- LiveLearn page: Enables a user to start or join a video conference
- LearningLinks page: Enables a user to view all LearningLinks
- Add LearningLink page: Enables a user to add a new LearningLink
- Edit LearningLink page: Enables a user to edit a created LearningLink
- Categories page: Enables a user to view all Categories of LearningLinks
- Add Category page: Enables a user to add a new Categories of LearningLinks
- Edit Categories page: Enables a user to edit a created Categories of LearningLinks

### Features Left to Implement
Milestone 4 will provide me with the skills to further control the access of users and there privileges contributing to the site. 

## Testing
- [JavaScript Validator](https://jshint.com/)
- [CSS Validator](http://csslint.net/)
- [HTML Validator](https://www.freeformatter.com/html-validator.html)

This site was tested across multiple browsers (Chrome, Safari, Internet Explorer, FireFox) and on multiple mobile devices (iPhone 4, 5, 7: Chrome and Safari, iPad, Samsung Galaxy) to ensure compatibility and responsiveness via [responsinator](https://www.responsinator.com/)

- Checked if each link on the home page lead to the correct web page
    - All links lead to the right web page
- Tested if adding LearningLink to the LearningLinks page worked and if a user was able to delete and edit them
    - Tests worked right, as I was able to add, edit and delete the LearningLink
- Tested if other web browsers could see the LearningLink added to the database
    - Test worked right, links posted and displayed    
- Tested if adding Category to the LearningLinks Categories page worked and if a user was able to delete and edit them
    - Tests worked right, as I was able to add, edit and delete a Category LearningLink
- Tested if other web browsers could see the Category LearningLink added to the database
    - Test worked right, Categories posted and displayed
- Tested if all the links in the footer, link to the correct pages by clicking on them
    - Tests worked correctly
- Tested if all the links in the sideNav, link to the correct pages by clicking on them
    - Tests worked correctly    
- Tested the responsiveness of the website through a phone and the Chrome DevTools on desktop 

### Media
All photos were taken from [unsplash](https://www.unsplash.com/), open source image library.

### Acknowledgements
All skills acquired from [codeInstitute](https://codeinstitute.net/), training source.
- [W3Schools](https://www.w3schools.com/python/python.asp)
- [mongoDB Documentation](https://docs.mongodb.com/manual/reference/method/db.collection/)
- [PyMongo Documentation](https://api.mongodb.com/python/current/api/pymongo/collection.html)
- [Stackoverflow](https://stackoverflow.com/)
- [MDN web docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/)

**This is for educational use.**