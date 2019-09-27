from django.db import models


class Skill(models.Model):
    title = models.CharField(max_length=100, null=False)


class User(models.Model):
    vk_id = models.IntegerField(null=False)
    balance = models.IntegerField(default=0)
    level = models.IntegerField(default=1)


class Category(models.Model):
    title = models.CharField(max_length=100, null=False)


class Quest(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    reward = models.IntegerField(default=0)
    categories = models.ManyToManyField(Category)
    is_quick = models.BooleanField(default=False)
    is_group = models.BooleanField(default=False)
    time_to_be_done = models.DateField(default=None)


class UserQuest(models.Model):
    status = models.IntegerField(default=0, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE)


class UserSkills(models.Model):
    status = models.IntegerField(default=0, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
