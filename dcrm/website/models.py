from django.db import models

# *** Remember: When you update the model, you must run:
#				python3 manage.py makemigrations
#				(The migration will be located in app/migrations for you to review)
#
#				Finally, run:
#				python3 manage.py migrate
# ***

# Define a record for the CRM database
class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	address = models.CharField(max_length=100)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	zipcode = models.CharField(max_length=20)

	# Define what values display when returning a new Record 
	def __str__(self):
		return(f"{self.first_name} {self.last_name}")
