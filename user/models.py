from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('users must has an email address')
        
        email = self.normalize_email(email)
        email = email.lower()
        
        user = self.model(
            email=email,
            name=name
        )
        user.set_password(password)
        user.save()
        
        return user
    
    def create_realtor(self, email, name, password=None):
        user = self.create_user(email, name, password)
        
        user.is_realtor = True
        
        user.save()
        
        return user
    
    def create_superuser(self, email, name, password=None):
        user = self.create_user(email, name, password)
        user.is_staff = True
        user.is_superuser = True

        user.save()
        
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    
    is_realtor = models.BooleanField(default=True)
    
    objects = UserAccountManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    def __str__(self):
        return self.email
    
    
class Listings(models.Model):
    
    class SaleType(models.TextChoices):
        FOR_SALE = 'for sale'
        FOR_RENT = 'for rent'
        
    title = models.CharField(max_length=255)
        
    name = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    main_photo = models.ImageField(upload_to='listings/')
    
    def __str__(self):
        return self.title
    
    
        
    
    
    