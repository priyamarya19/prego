from django.db import models

# Create your models here.

class Contact(models.Model):
	number=models.IntegerField(blank=False,null=False)
	count=models.IntegerField(blank=True,null=True)

	class Meta:
		verbose_name = "Contact"
		verbose_name_plural = "Contact"

	def __str__(self):
		return str(self.number)