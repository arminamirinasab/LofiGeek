from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

from core.settings import BASE_DIR

import os

class Music(models.Model):
    title = models.CharField(max_length=300)
    song_file = models.FileField(upload_to='audios/', null=False, blank=False)
    song_cover = models.ImageField(upload_to='covers/', default='covers/default/d_cover.jpg')


    def __str__(self) -> str:
        return self.title
    

@receiver(post_delete, sender=Music)
def delete_related_filse(sender, instance, **kwargs):
    if instance.song_file:
        os.remove(instance.song_file.path)

    if instance.song_cover and instance.song_cover.path != f'{BASE_DIR}\media_cdn\covers\default\d_cover.jpg':
        os.remove(instance.song_cover.path)