# Profiles REST API

## python -m venv ~/env

## Django creates Migration files to store all the steps required to match db with django model

## change/add model then have to create new migration file
## (env) vagrant@ubuntu-bionic:/vagrant$ python manage.py makemigrations django_profiles_api 

## run migrations like in RoR after creating migrations :)
## (env) vagrant@ubuntu-bionic:/vagrant$ python manage.py migrate
## Each model in our Django maps to a specific table in our database
## No need to write any sequal statements coz Django manages the relation between model and db.
## Serializers also check the validation
## POST functionality to APIView

## Data in json format http://127.0.0.1:8000/api/hello-view/?format=json
## APIView and VIEWSETS classes allow us to write our logic 
## APIView (HTTP funcs) have also CRUD and ViewSets(Actions to perform) also have CRUD but offer diff and additional operations
## When to use ViewSets and when to use APIView
## register viewsets with urls is slighly diff than registering APIView with urls

## URL retrieving functions provided by Django.
## http://127.0.0.1:8000/api/hello-viewset/, http://127.0.0.1:8000/api/hello-viewset/?format=json

## http://127.0.0.1:8000/api/hello-viewset/1/
