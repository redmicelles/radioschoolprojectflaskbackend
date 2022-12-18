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

# Working Directly with Alembic?
- Create Environment
  alembic init alembic

# Docker Compose
- MSQL Service is preferred
- Postgre and PG-Admin are disabled but may be enable and environment variables set to meet requirements

# JWT RS256 Keys
Access tokens are signed using RS256 private keys and are decoded using the public keys. These keys can be generated using OpenSSL by following the steps below
- generate a private key with the correct length
openssl genrsa -out private-key.pem 3072

- generate corresponding public key
openssl rsa -in private-key.pem -pubout -out public-key.pem

- optional: create a self-signed certificate
openssl req -new -x509 -key private-key.pem -out cert.pem -days 360

- optional: convert pem to pfx
openssl pkcs12 -export -inkey private-key.pem -in cert.pem -out cert.pfx

source1: https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth_key_and_cert.htm
source2: https://www.scottbrady91.com/openssl/creating-rsa-keys-using-openssl

# Black for Code fromatting
https://pypi.org/project/black/
- to format codebase run `black .` from the root
