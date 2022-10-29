from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=300, db_collation='utf8_general_ci', blank=True, null=True)
    isbn = models.CharField(db_column='ISBN', primary_key=True, max_length=17, db_collation='utf8_general_ci')  # Field name made lowercase.
    author = models.CharField(max_length=306, db_collation='utf8_general_ci', blank=True, null=True)
    description = models.CharField(max_length=15000, db_collation='utf8_general_ci', blank=True, null=True)
    link = models.CharField(max_length=300, db_collation='utf8_general_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'books'