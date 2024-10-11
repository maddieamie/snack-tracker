# LAB - Class 27
**Project:** Django Snack Tracker  
**Author:** Maddie Amelia Lewis

## Links and Resources
- **Back-end Server URL**: Not applicable
- **Front-end Application**: Not applicable

## Setup

### .env requirements (where applicable)
- None required for this lab

### How to initialize/run your application
- To run the Django development server:


 python manage.py runserver

#### To create and apply database migrations:

python manage.py makemigrations

python manage.py migrate

#### To create a superuser for the Django Admin:

python manage.py createsuperuser

#### How to use your application
**Snack List:**
Navigate to the home page to see a list of snacks.

**Snack Detail:**
Click on a snack name to view its detail page, which shows the name, description, and purchaser.

**Admin Panel:**
Go to /admin/ to add, edit, or delete snacks.


### Tests

**How do you run tests?**
To run the Django tests:


python manage.py test

**Any tests of note?**

*Tested views for:*

- Status code validation (200 OK)
- Correct template rendering for both the snack list and snack detail views
- Tests use reverse() for URL pattern matching.

*Describe any tests that you did not complete, skipped, etc.*

Testing for SnackDetailView requires creating snack objects via fixtures or setup methods, but the focus was on foundational testing in this lab.