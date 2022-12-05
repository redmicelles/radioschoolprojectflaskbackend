#Startup Postgre Docker Container
docker-compose up --build -d

#Startup Environment
pipenv shell
pipenv install

#Startup Flask App Server
python3 run.py
