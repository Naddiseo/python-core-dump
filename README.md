To start:
```bash
# Run this in one terminal
docker-compose build
docker-compose up
# Then this in another
docker-compose exec web python manage.py migrate
```

Then in a webbrowser, go to http://127.0.0.1:8877
