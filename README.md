# About

Minimal reproducible example of
[django-filter issue 1103](https://github.com/carltongibson/django-filter/issues/1103).


# See it in action

```
git clone https://github.com/moseb/django-filter-issue-1103-demo.git
cd django-filter-issue-1103-demo

virtualenv --python=python3.7 .py37
source .py37/bin/activate
pip install -r requirements.txt
./manage.py migrate
./manage.py runserver &
wget -O- http://127.0.0.1:8000/products/?tags__in=1,0
```
