from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title


    class Meta:
        db_table = 'Counters'  # 数据库表名
