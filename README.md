# NonAlco4Me


![]()

Please view the live website here: [NonAlco4Me](https://non-alco-4me-427be0bd27b2.herokuapp.com/ "NonAlco4Me Homepage").

## Table of contents
+ [UX](#ux)
  + [Site Purpose](#site-purpose)
  + [Site Goal](#site-goal)
  * [Audience](#audience)
  * [Communication](#communication)
  * [Current User Goals](#current-user-goals)
  * [New User Goals](#new-user-goals)
  * [Future Goals](#future-goals)
* [User Stories](#user-stories)
  * [Pilot](#pilot)
  * [Admin](#admin)
* [Design](#design)
  * [Wireframes](#wireframes)
  * [Site Navigation](#site-navigation)
  * [Database Schema](#database-schema)
  * [Color Scheme](#color-scheme)
  * [Typeography](#typography)
  * [Imagery](#imagery)
* [Features](#features)
  * [Homepage](#homepage)
  * [Recipes Home](#recipes-home)
  * [Site Detail](#site-detail)
  * [Contact](#contact-page)
  * [Sign-In](#sign-in)
  * [Sign-Out](#sign-out)
  * [Sign-Up](#sign-up)
* [C.R.U.D.](#crud)
  * [Create](#create)
  * [Read](#read)
  * [Update](#update)
  * [Delete](#delete)
* [Future Features](#future-features)
* [Manual Testing](#manual-testing)
* [Automated Testing](#automated-testing)
* [Validator Testing](#fixed-bugs)
* [Accessibility](#accessibility)
* [Technologies Used](#technologies-used)
* [Deployment](#deployment)
* [Credits](#credits)

## UX
### Site Purpose


### Site Goal


### Audience


### Communication


### Current User Goals


### New User Goals


### Future Goals


## Epics


## User Stories


### Pilot 


### Admin


## Design
### Wireframes
![]()


### Site Navigation
![]()

### Database Schema
![]()

### Color Scheme
![]()

### Typography:


### Imagery:


## Features
### Homepage


### Recipes Sites


### Recipes detail



### Contact Page


### Sign-in


### Sign-out


### Sign-up


## C.R.U.D.
### Create
### Site Upload



### Site comments (gallery comments are the same)


## Read


## Update


### Edit Site


## Delete

### Delete Recipe


## Future features


## Manual Testing
### Homepage


### Recipes Home



### Comments


## Automated testing


### Browsers

## Validator Testing
- HTML files pass through the W3C validator with no issues found.
- CSS files pass through the Jigsaw validator with no issues found.
- Python files have been through the validator and have no issues.

## Fixed bugs


## Accessibility


## Technologies Used
### Main Languages Used
- HTML5
- CSS3
- Python
- Django
- SQL - Postgres

### Frameworks, Libraries & Programs Used
- Google Fonts - for the font families:
- Font Awesome - to add icons to the social links in the footer element.
- VSC - to edit my code before pushing the project to Github.
- GitHub - to store my repository for submission.
- Balsamiq - were used to create mockups of the project prior to starting.
- Am I Responsive? - to ensure the project looked good across all devices.
- Favicon - to provide the code & image for the icon in the tab bar.
- Django
- Bootstrap
- DrawSQL

### Installed Packages:
- 'django<4' gunicorn
- dj_database_url psycopg2
- dj3-cloudinary-storage
- django-summernote (link)
- django-allauth (link)
- django-crispy-forms(link)

## Deployment
The site was deployed to Heroku. The steps to deploy are as follows:

- Install Django & Gunicorn: pip3 install 'django<4' gunicorn
- Install Django database & psycopg: pip3 install dj_database_url psycopg2
- Install Cloudinary: pip3 install dj3-cloudinary-storage
- Creating the requirements.txt file with the following command: pip3 freeze --local > requirements.txt
- A django project was created using: django-admin startproject printstatements 
- The Hillbox app was then created with: python3 manage.py startapp blog
- Which was then added to the settings.py file within our project directory
- The changes were then migrated using: python3 manage.py migrate.
- Navigated to Heroku & created a new app called print-statements.
- Added the Heroku Postgres database to the Resources tab.
- Navigated to the Settings Tab, to add the following key/value pairs to the configvars:
key: SECRET_KEY | value: randomkey
key: PORT | value: 8000
key: CLOUDINARY_URL | value: API environment variable
key: DATABASE_URL | value: value supplied by Heroku
- Added the DATABASE_URL, SECRET_KEY & CLOUDINARY_URL to the env.py file 
- Added the DATABASE_URL, SECRET_KEY & CLOUDINARY_URL to the settings.py file
- Add an import os statement for the env.py file.
- Added Heroku to the ALLOWED_HOSTS in settings.py
- Created the Procfile
- Pushed the project to Github
- Connected my github account to Heroku through the Deploy tab
- Connected my github project repository, and then clicked on the "Deploy" button

The live link for "NonAlco4Me" can be found [HERE](https://non-alco-4me-427be0bd27b2.herokuapp.com/)

## Credits
### Content


## Images
