from django.db import models

class Question(models.Model):
    CATEGORY_CHOICES = [
        ('Python', 'Python'),
        ('SQL', 'SQL'),
        ('Django', 'Django'),
        ('Other', 'Other'),
    ]

    text = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category}: {self.text[:50]}"
