from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser


# Create your models here.
def user_image_path(instance, filename):
    return '/'.join(['media/profile_pics/', str(instance.id), filename])


class TwitterUserManager(BaseUserManager):

    def create_user(self, username, email, first_name, last_name, password=None):
        if not email:
            raise ValueError('E-mail is mandatory')

        if not username:
            raise ValueError('User name is mandatory')

        if not first_name:
            raise ValueError('First Name is mandatory')

        if not last_name:
            raise ValueError('Last Name is mandatory')

        user = self.model(email=email, first_name=first_name, last_name=last_name, username=username)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, first_name, last_name, password):

        user = self.create_user(first_name=first_name, last_name=last_name, email=self.normalize_email(email),
                                username=username, password=password)

        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True, max_length=200)
    about = models.TextField(null=True)
    image_url = models.FileField(upload_to=user_image_path, null=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now_add=True)
    objects = TwitterUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    def __str__(self):
        return str(self.id)

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return True


class Follow(models.Model):
    id = models.AutoField(primary_key=True)
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following_user')
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User {self.follower} | Following {self.following}"


def user_image_path(instance, filename):
    return '/'.join(['uploads/resumes/', str(instance.id), filename])
