from django.db import models
import datetime
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    created_at = models.DateField(default=datetime.date.today)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    
    def time_passed(self):
        return (datetime.date.today() - self.created_at ).days
    
        # other possibility for writing this function
        # def time_passed(self):
        #     today = datetime.date.today()
        #     delta = today - self.created_at
        #     return delta.days

    