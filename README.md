# radioschoolprojectflaskbackend
Flask Backend API for Radio School

# App Structure guide
https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy
https://abstractkitchen.com/blog/flask-backbone/

# Create New Virtual Environment
- pipenv install

# For Pipenv pipenv.exceptions.ResolutionFailure
- pipenv --rm (Remove Virtual Environment)
- rm Pipfile* (Remove Pip files)
- pipenv shell (To create a new Venv)
- manually install all requirement using pipenv install

# Launch PIPENV
- pipenv shell

# Generate Lock File Dependencies from Requirements.txt
pipenv install -r requirements.txt

# Flask Migrate
- Initialise Migration Scripts
  flask --app app_config db init
- Migrate DB Changes
  flask --app app_config db migrate
- DB Pre-Upgrade Script (optional)
  flask --app app_config db stamp head
- Upgrade Db
  flask --app app_config db upgrade

# Working Directly with Alembic
- Create Environment
  alembic init alembic

# Docker Compose
- MSQL Service is preferred
- Postgre and PG-Admin are disabled but may be enable and environment variables set to meet requirements

# Running the app
- python flask_app.py