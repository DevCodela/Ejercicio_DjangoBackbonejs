from django.db import models


class Libro(models.Model):

    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    edicion = models.IntegerField(default=1)

    def __unicode__(self):
        
        return "%s por %s" % (self.titulo, self.autor,)