from django.db import models
from django.utils import timezone
import datetime

class Blog(models.Model):
	title = models.CharField(max_length=100)
	blog = models.TextField(blank=False)
	description = models.CharField(max_length=500, default='No Description Available')
	pub_date = models.DateField("Date Published")

	def __str__(self):
		return self.title

	def was_published_recently(self):
		return self.pub_date >= timezone.now()
datetime.timedelta(days=1)
