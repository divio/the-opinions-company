The Opinions Company - a simple project to demonstrate Divio Cloud migration
============================================================================


Set the project up locally
--------------------------

Clone the project, and cd into the directory::

    git clone git@github.com:divio/the-opinions-company.git
    cd the-opinions-company

Create and activate a virtual environment::

    python3.6 -m venv env
    source env/bin/activate

Install the project's dependencies into the virtual environment::

    pip install -r requirements.txt

Run migrations to create the empty database tables::

    python manage.py migrate

Load the database content from the ``database.json`` file::

    python manage.py loaddata database.json

Start the runserver::

    python manage.py runserver

You can now open the site at http://localhost:8000

Username and password: ``admin``/``admin``.


Migrate to Divio Cloud
----------------------
