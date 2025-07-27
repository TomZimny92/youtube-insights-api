from django.db import models

class Channel(models.Model):
    id = models.TextField().primary_key=True
    title = models.TextField()
    description = models.TextField()
    customUrl = models.TextField()
    datePublished = models.DateTimeField()
    thumbnail = models.TextField()
    statistics = models.JSONField()

    def __str__(self):
        return self.title
    
class Video(models.Model):
    id = models.TextField().primary_key=True
    title = models.TextField()
    channelTitle = models.TextField()
    publishedAt = models.DateTimeField()
    thumbnail = models.TextField()
    views = models.IntegerField()
    likes = models.IntegerField()
    favorites = models.IntegerField()
    comments = models.IntegerField()
    engagementRate = models.FloatField()

    def __str__(self):
        return self.title