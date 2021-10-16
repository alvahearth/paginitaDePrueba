from django.contrib.auth.models import User
from .models import PerfilDelUsuario
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save

@receiver(post_save, sender=User)
def crear_perfil(sender, instance, created, **kwargs):
    if created:
        PerfilDelUsuario.objects.create(user=instance)

@receiver(post_save, sender=User)
def actualizar_perfil(sender, instance, **kwargs):
     instance.perfildelusuario.save()