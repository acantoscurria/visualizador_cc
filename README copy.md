
docker-compose -f local.yml build

docker-compose -f local.yml up

docker-compose -f local.yml run --rm django python manage.py makemigrations

docker-compose -f local.yml run --rm django python manage.py showmigrations

docker-compose -f local.yml run --rm django python manage.py migrate

docker-compose -f local.yml run --rm django python manage.py startapp dashboard $PWD/dashboard

docker-compose -f local.yml run --rm django mkdir $PWD/dashboard

456258jose