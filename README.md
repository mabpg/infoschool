# infoschool
#Informatizandote 0.15

#Instalación
sudo apt-get install postgresql-server-dev-9.3
sudo apt-get install python-dev

pip install -r requirements.txt
python manage.py syncdb
python manage.py runserver
