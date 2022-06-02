
docker compose -f production.yml build

docker compose -f production.yml up

docker compose -f production.yml run --rm django python manage.py makemigrations

docker compose -f production.yml run --rm django python manage.py showmigrations

docker compose -f production.yml run --rm django python manage.py migrate

docker compose -f production.yml run --rm django python manage.py startapp dashboard $PWD/dashboard

docker compose -f production.yml run --rm django mkdir $PWD/dashboard

docker compose -f production.yml run --rm django python manage.py inspectdb con_matric_comun_primaria --include-views > model_temp.py


docker compose -f production.yml run --rm django python manage.py createsuperuser

docker compose -f production.yml run --rm django python manage.py shell_plus



docker compose -f production.yml run --rm django python manage.py collectstatic

docker compose -f production.yml run --rm django python manage.py collectstatic --clear

docker compose -f production.yml run --rm django python manage.py collectstatic --noinput --clear

docker compose -f production.yml run --rm django python manage.py showmigrations

docker compose -f production.yml run --rm django python manage.py makemigrations


# Linux
sudo apt-get install python3-venv    # If needed
python3 -m venv .venv
source .venv/bin/activate
https://code.visualstudio.com/docs/python/tutorial-django

admin
admin