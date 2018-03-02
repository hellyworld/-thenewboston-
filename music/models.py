from django.db import models
from django.core.urlresolvers import reverse


# Red pk 1 (primary key)
class Album(models.Model):
    artist = models.CharField(max_length=100)
    album_title = models.CharField(max_length=150)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()

    def get_absolute_url(self):
        # 'music detail' is the first parameter - the view name
        return reverse('music:detail', kwargs={'pk': self.pk})  # new album > add to DB > pk > detail view

    def __str__(self):  # what it must show us
        return self.album_title + '-' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    # CASCADE - on Album delete, all Song delete
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
