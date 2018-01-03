# Olist Challenge

This Django app was made for a chalenge proposed by Olist for a job position.
The main purpose of the application is to develop a category system with channels.
Each channel has his own categories and the categories can be nested from 0 to N levels.

#### Environment used

The whole app was developed on MAC OS X using Atom as text editor. Also, Docker was used to provide a easy way to setup Postgres once the project uses it as database.

The following libraries was used on the project.
--- Django - web framework;
--- Django Rest Framework -  framework build on top of Django for API development;
--- Django Environ - library that allows you to utilize 12factor inspired environment variables to configure your Django application;
--- Whitenoise - static file serving for Python web apps;
--- Psycopg2 - postgres adapter for python.
##### Debug
--- Django Debug Toolbar - A configurable set of panels that display various debug information about the current request/response. (Extremely useful for query time analysis).

### Running the tests

```
./manage.py test channels
```

### API
A demo of the project was hosted on Heroku at https://serene-earth-21150.herokuapp.com

##### Channels
- <GET> **/api/v1/channel/** - List all channels
- <GET> **/api/v1/channel/<uuid>** - Show details of a channel. Also shows parent categories in categories.
-- <uuid> Unique identifier of the channel used to avoid exposing the database ID

##### Categories
- <GET> **/api/v1/category/** - List all categories
- <GET> **/api/v1/category/<uuid>** - Show details of a category with parents.
-- <uuid> Unique identifier of the category used to avoid exposing database ID
