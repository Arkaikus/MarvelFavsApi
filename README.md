# MarvelFavsApi

This simple API lets you manage your favorite comics from MARVEL

## Setup

For development

- Download the repo with `git clone`
- Create a virtualenv with `virtualenv venv -p python3`
- Activate virtualenv
- Install requirements with `pip install -r requirements.txt`
- Then `cd app`
- Run app with `python manage.py runserver host:port`

## Deploy

For deployment

### Heroku

Fork this repository, then link it to your own heroku app with `heroku git:remote -a <app-name>` and deploy from
heroku site or pushing to heroku remote

### Docker

Run `make build` to create the docker image, then run `make run` to start the container of the api

the container runs on port `9080` feel free to change it in `docker/docker-compose-yml`

## Endpoints

Check `host:port/doc` for swagger documentation

## Licence

MIT License  
Check the LICENCE file