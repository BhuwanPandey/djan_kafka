from django.db import models


class FaceEmbed(models.Model):
    age = models.IntegerField()
    emotion = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"FaceEmbed -> {self.id}"
