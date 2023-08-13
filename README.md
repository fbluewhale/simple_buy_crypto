## About The Project
this is a simple project for set order to buy crypto


#### Built With:
  - python
  - django
  - drf
  - sqlite - postgresql
   ------------------------------------
#### Documentation:
    after running the server.
    find out the bellow path:
    http://127.0.0.1:8000/swagger/
#### Install locally
```bash
python -m venv env
source env/bin/activate
git clone git@github.com:fbluewhale/simple_buy_crypto.git
cd simple_buy_crypto
pip install -r requirements.txt
```

Migrate database and run project:
```
python manage.py migrate
python manage.py runserver
```

run celery:
```
celery -A config beat
celery -A config  worker -l info
```
run tests:
```
python manage.py test
```

# Note:
in this project, all relations are protected for the importance of user trade history