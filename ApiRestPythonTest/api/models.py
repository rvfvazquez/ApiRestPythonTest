from django.db import models

# Create your models here.
class FeiraLivre(models.Model):
    ID          = models.AutoField(primary_key=True)
    LONG        = models.IntegerField
    LAT         = models.IntegerField
    SETCENS     = models.IntegerField
    AREAP       = models.IntegerField
    CODDIST     = models.IntegerField
    DISTRITO    = models.CharField(db_index=True,max_length=80)
    CODSUBPREF  = models.IntegerField
    SUBPREFE    = models.CharField(max_length=45)
    REGIAO5     = models.CharField(db_index=True,max_length=45)
    REGIAO8     = models.CharField(max_length=45)
    NOME_FEIRA  = models.CharField(db_index=True,max_length=150)
    REGISTRO    = models.CharField(db_index=True,max_length=50)
    LOGRADOURO  = models.CharField(max_length=155)
    NUMERO      = models.CharField(max_length=45)
    BAIRRO      = models.CharField(db_index=True,max_length=150)
    REFERENCIA  = models.CharField(max_length=45)



    def save(self, *args, **kwargs):
            return super(FeiraLivre, self).save(*args, **kwargs)

    
    def __str__(self): 
        return self.REGISTRO + self.NOME_FEIRA
            