This project is a small demonstration of django skills.

Requirements are listed in requirements.txt

To run project do the following steps:

*1. Create migrations for app library using next command series*\
`python manage.py makemigrations library`\
`python manage.py makemigrations`\
`python manage.py migrate`\
*2. To run sync version (without statistics) use:*\
`python manage.py runserver`\
*3. To run async version (with statistics) use:*\
`uvicorn django_usage.asgi:application`

*4 (optional). To load test fixtures use:*
`python manage.py loaddata <path_to_fixture>`

Fixtures are stored in test_fixtures dir

To run tests use:
`python manage.py test library.tests`

For proper usage please check library/urls.py file. `/library/` url uses \
pagination, so template to demonstrate it is stored in templates dir