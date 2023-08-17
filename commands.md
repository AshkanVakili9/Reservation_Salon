
# Generate new secret key

python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"


py -m venv venv

venv\scripts\activate


pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py generate_city
python manage.py createsuperuser


pytest --cov

pipenv install git+https://github.com/sageteam-org/django-iranian-cities.git#egg=django-iranian-cities
