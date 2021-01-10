from django.db import models


class Bookmarks(models.Model):
    repo_id = models.CharField(max_length=100)
    bookmarked = models.BooleanField()

    class Meta:
        db_table = "bookmarks"
