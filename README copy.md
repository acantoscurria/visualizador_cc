
docker-compose -f local.yml build

docker-compose -f local.yml up

docker-compose -f local.yml run --rm django python manage.py makemigrations

docker-compose -f local.yml run --rm django python manage.py showmigrations

docker-compose -f local.yml run --rm django python manage.py createsuperuser

docker-compose -f local.yml run --rm django python manage.py migrate

docker-compose -f local.yml run --rm django python manage.py startapp dashboard $PWD/dashboard

docker-compose -f local.yml run --rm django mkdir $PWD/dashboard


# Linux
sudo apt-get install python3-venv    # If needed
python3 -m venv .venv
source .venv/bin/activate


admin
admin@admin.com
456258

jose
456258Jose