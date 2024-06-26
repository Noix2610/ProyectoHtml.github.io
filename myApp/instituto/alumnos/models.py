from django.db import models # type: ignore

# Create your models here.
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=20)
    nom_usuario = models.CharField(max_length=20)
    telefono = models.CharField(max_length=45)
    email = models.EmailField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    id_profesion = models.ForeignKey('Profesion',on_delete=models.CASCADE, db_column='id_profesion')
    region = models.CharField(max_length=50, blank=True, null=True)
    ciudad = models.CharField(max_length=50, blank=True, null=True)
    cod_postal = models.IntegerField()
    #Se comenta ya que da problema con la migración value=9
    # id_tipo_usuario = models.ForeignKey('Tipo_usuario',on_delete=models.CASCADE, db_column='id_tipo_usuario')

    def __str__(self):
        return str(self.nombres)+" "+str(self.apellidos)
    
class Profesion(models.Model):
    id_profesion = models.AutoField(db_column='id_profesion', primary_key=True)
    profesion = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.profesion)

class Tipo_usuario(models.Model):
    id_tipo_usuario = models.IntegerField(primary_key=True)
    descripcion =models.CharField(max_length=400, blank=False, null=False)

    def __str__(self):
        return str(self.id_tipo_usuario)

class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    nombre_categoria = models.CharField(max_length=50,blank=False, null=False)

    def __str__(self):
        return str(self.Categoria)
