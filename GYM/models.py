from datetime import datetime

from django.db import models

class Contact(models.Model):
  name = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  message = models.CharField(max_length=555)
  created_at = models.DateTimeField(auto_now_add=True)

class users(models.Model):
  id = models.IntegerField(primary_key=True)
  name = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  password = models.CharField(max_length=555)
  created_at = models.DateTimeField(auto_now_add=True)

class packages(models.Model):
  heading1 = models.CharField(max_length=255)
  heading2 = models.CharField(max_length=255)
  list = models.CharField(max_length=855)
  price = models.CharField(max_length=222)
  created_at = models.DateTimeField(auto_now_add=True)

class subscribed(models.Model):
  u_id = models.ForeignKey("users", on_delete=models.CASCADE)
  p_id = models.ForeignKey("packages", on_delete=models.CASCADE)
  paid = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)

