from django.db import models

# Create your models here.


class Projects(models.Model):
    project_Name = models.CharField(max_length=100)
    Develop_By = models.CharField(max_length=100)
    Develop_For = models.CharField(max_length=100)
    Start_date = models.DateTimeField()
    End_date = models.DateTimeField()

    def __str__(self):
        return self.project_Name