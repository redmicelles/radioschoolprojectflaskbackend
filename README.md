# radioschoolprojectflaskbackend
Flask Backend API for Radio School

# App Structure guide
https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy
https://abstractkitchen.com/blog/flask-backbone/

# Launch PIPENV
pipenv shell

# Generate Lock File Dependencies from Requirements.txt
pipenv install -r requirements.txt

# Flask Migrate
- Initialise Migration Scripts
  flask --app run db init
- Migrate DB Changes
  flask --app run db migrate
- DB Pre-Upgrade Script (optional)
  flask --app run db stamp head
- Upgrade Db
  flask --app run db upgrade