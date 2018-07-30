web: gunicorn app:app
release: python app.py db init
release: python app.py db migrate
release: python app.py db upgrade