from django.db import models

class Note(models.Model):
    COLOR_CHOICES = [
        ('R', 'red'),
        ('B', 'blue'),
        ('G', 'green'),
        ('Y', 'yellow'),
        ('W', 'white')
    ]
    name = models.CharField(max_length=127)
    color = models.CharField(max_length=1, choices=COLOR_CHOICES, default='W')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class NoteParagraph(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, 
                            related_name='paragraphs')
    body = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.body[:50]