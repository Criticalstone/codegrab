from django.db import models

class Code(models.Model):
    code = models.CharField(db_column='CODE', primary_key=True, max_length=100)
    claimed = models.IntegerField(db_column='CLAIMED')