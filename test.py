import datetime
import os
import django
os.environ["DJANGO_SETTINGS_MODULE"] = "movies.settings"
django.setup()

from movies_app.models import Movie, Director

if __name__ == '__main__':
    # Movie(name="Titanic", year=2000).save()
    # movie = Movie.objects.get(id=1)
    # # director = Director.objects.create(name="James Cameron", birth_date=datetime.date(1957, 8, 16))
    # # print(director)
    # movie.director = Director.objects.get(id=1)
    # movie.save()


