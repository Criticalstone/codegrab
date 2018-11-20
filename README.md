# Codegrab
a simple web app to distribute codes to, for example, games.
The list of codes can be submitted in csv format by some admin and are protected from the users.

Observe: There is no guard for a user to get more than one code. This is not needed for my use but feel free to fork this and implement it.

## Starting the server
`python manage.py migrate` to migrate database

`python manage.py createsuperuser` to create an admin user

`python manage.py runserver <port>`to start server 

Then navigate to `ip:<port>/add` to upload a csv of the codes that should be available.
Users then access the root page to get a unique code
