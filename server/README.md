# UPBEAT SERVER

Install posgres to your local machine

Setup posgres, add username and password

# Create a database

# Install packages by running the command
pip install -r requirements.txt

# Add the following to env to get the app started
export DB_USERNAME
export DB_PASSWORD
export DB_HOST
export DB_NAME
export FLASK_SECRET_KEY
export SPOTIFY_CLIENT_ID
export SPOTIFY_CLIENT_SECRET
export MAIL_SERVER
export MAIL_PORT
export MAIL_USERNAME
export MAIL_PASSWORD
export MAIL_SALT
\

# Create a virtualenv to containerize the app
virtualenv <venv>
 source <venv>/Scripts/activate    <!-- for windows -->
 source <venv>/bin/activate        <!-- for linux -->

# On the root director start app by running
python run.py


## Setting up alembic

- install alembic
    pip install
- initialize alembic migrations
    alembic init migrations
- Congigure alembic.ini file
    update db url
- create a version
    alembic revision --autogenerate -m 'initial model setup'
- commit version to db
    alembic upgrade heads


