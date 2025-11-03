from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _

class Cargo_Empleado(models.Model):
    id_Cargo = models.AutoField(primary_key=True)
    Nombre_Cargo = models.CharField(max_length=50)

class Area(models.Model):
    id_Area = models.AutoField(primary_key=True)
    Nombre_Area = models.CharField(max_length=100)
    Descripcion = models.TextField()

class Departamento(models.Model):
    id_Departamento = models.AutoField(primary_key=True)
    Nombre_Departamento = models.CharField(max_length=100)


class Cliente(models.Model):
    id_Cliente = models.AutoField(primary_key=True)
    Nombre_Cliente = models.CharField(max_length=100)
    Razon_Social = models.CharField(max_length=150)
    Numero_Ruc = models.CharField(max_length=20)
    Tipo = models.CharField(max_length=50)  

class Empleado(models.Model):
    id_Empleado = models.AutoField(primary_key=True)
    Nombre_Empleado = models.CharField(max_length=100)
    Email = models.EmailField()
    Telefono = models.CharField(max_length=20)
    Fecha_Contratacion = models.DateField()
    id_Cargo = models.ForeignKey(Cargo_Empleado, on_delete=models.SET_NULL, null=True)
    id_Area = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True)
    id_Departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True)
    id_Cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True) 

class Contacto_Empresa(models.Model):
    id_Contacto = models.AutoField(primary_key=True)
    Nombre_Contacto = models.CharField(max_length=100)
    Cargo_Contacto = models.CharField(max_length=100)
    id_Cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, related_name='Contactos')


class Tipo(models.Model):
    id_Tipo = models.AutoField(primary_key=True)
    Mobiliario = models.CharField(max_length=100)
    Rotulacion = models.CharField(max_length=100)

class Estado_Proyecto(models.Model):
    id_Estado = models.AutoField(primary_key=True)
    Estado_Actual = models.CharField(max_length=50)

class Proyecto(models.Model):
    id_Proyecto = models.AutoField(primary_key=True)
    Nombre_Proyecto = models.CharField(max_length=100)
    Fecha_Creacion = models.DateField()
    Direccion = models.TextField()
    id_Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='Proyectos')
    id_Estado = models.ForeignKey(Estado_Proyecto, on_delete=models.SET_NULL, null=True)
    id_Proforma = models.ForeignKey('Proforma', on_delete=models.SET_NULL, null=True)

class Proforma(models.Model):
    id_Proforma = models.AutoField(primary_key=True)
    Descripcion = models.TextField()
    Taza_Cambio = models.DecimalField(max_digits=10, decimal_places=4)
    Fecha_Elaboracion = models.DateField()
    Fecha_Aprobacion = models.DateField(null=True, blank=True)

class Item(models.Model):
    id_Item = models.AutoField(primary_key=True)
    Dimensiones = models.CharField(max_length=100)
    Precio = models.DecimalField(max_digits=10, decimal_places=2)
    Descuento = models.DecimalField(max_digits=5, decimal_places=2)
    Cantidad = models.IntegerField()
    id_Proforma = models.ForeignKey(Proforma, on_delete=models.CASCADE, related_name='Items')

class Proveedores(models.Model):
    id_Proveedor = models.AutoField(primary_key=True)
    Nombre_Proveedor = models.CharField(max_length=100)
    Direccion = models.CharField(max_length=200)
    Telefono = models.CharField(max_length=20)
    Email = models.EmailField()

class Material_Compra(models.Model):
    id_Material = models.AutoField(primary_key=True)
    Nombre_Material = models.CharField(max_length=100)
    Cantidad = models.IntegerField()
    id_Item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='Materiales')
    id_Proveedor = models.ForeignKey(Proveedores, on_delete=models.SET_NULL, null=True)


