from django.db import models

from django.conf import settings

class Account(models.Model):
	id = models.BigAutoField(primary_key=True)
	owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        to_field='username'
    )
	class AccountType(models.IntegerChoices):
		TEACHER = 1
		STUDENT = 2
	accountType = models.IntegerField(choices=AccountType.choices)

class Scores(models.Model):
	student_id = models.ForeignKey(Account, on_delete=models.CASCADE,);
	subject = models.TextField();
	scores = models.IntegerField();
