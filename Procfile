release: python3 manage.py collectstatic --noinput && python3 manage.py migrate --noinput
web: gunicorn e_commerce_pbp.wsgi