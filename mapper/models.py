from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class Workspace(models.Model):
    WORKSPACE_STAGE_CHOICES = (
        ('__','Неизвестно'),
        ('1R','Первый этаж правое крыло'),
        ('1L','Первый этаж левое крыло'),
        ('2R','Второй этаж правое крыло'),
        ('2L','Второй этаж левое крыло'),
        ('3R','Третий этаж правое крыло'),
        ('3L','Третий этаж левое крыло'),
        ('4R','Четвертый этаж правое крыло'),
        ('4L','Четвертый этаж левое крыло'),
    )
    stage = models.CharField("Этаж, крыло",max_length=2, choices=WORKSPACE_STAGE_CHOICES, default="__")
    workspaceNum = models.CharField(max_length=2,blank=True)
    ip = models.GenericIPAddressField(protocol='IPv4',unpack_ipv4=False,unique=True)
    phone = models.CharField(max_length=6,blank=True)
    login = models.CharField(max_length=20,blank=True)
    xPos = models.PositiveSmallIntegerField()
    yPos = models.PositiveSmallIntegerField()
    status = models.PositiveSmallIntegerField(default=0)
    created_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.stage+str(self.id)+" ........ "+str(self.ip)+" ......... "+str(self.phone)

class Worker(models.Model):
    login = models.CharField(max_length=20,blank=True)
    name = models.CharField(max_length=20,blank=True)
    surname = models.CharField(max_length=20,blank=True)
