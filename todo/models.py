from django.db import models
from django.contrib.auth.models import User

import datetime
# Create your models here.
TYPE_CHOICES = (
	('PERSONAL','PERSONAL'),
    ('WORK', 'WORK')
	)

PRIORITY_CHOICES = (
    ('HIGH','HIGH'),
    ('MEDIUM', 'MEDIUM'),
    ('LOW','LOW')
)

class Task(models.Model):
	
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	task_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='PERSONAL')
	task_date = models.DateField()
	task_text = models.CharField(max_length=100)
	task_priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='LOW')
	task_status = models.BooleanField(default=False)

	def __str__(self):
		return self.task_text