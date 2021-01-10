from django.db import models

# Create your models here.
class Menu(models.Model):
    mid = models.AutoField(primary_key=True)
    mname = models.CharField(max_length=30,unique=True)

    def __unicode__(self):
        return u'Menu:%s'%self.mname
    class Meta:
        db_table = 't_menu'