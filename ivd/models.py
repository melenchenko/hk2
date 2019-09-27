from django.db import models


class Skill(models.Model):
    title = models.CharField(max_length=100, null=False)


class City(models.Model):
    title = models.CharField(max_length=100, null=False)


class User(models.Model):
    vk_id = models.IntegerField(null=False)
    balance = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    gender = models.SmallIntegerField(null=False, default=1) #0 - girl, 1 - boy
    speak_english = models.BooleanField(default=False)
    age = models.IntegerField(null=True)
    cloth_size = models.CharField(max_length=4, default='') #XS, ... , XXXL


class BlackList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    banned_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='banned_user')


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
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, default=None)
    longitude = models.FloatField(null=True, default=None)
    latitude = models.FloatField(null=True, default=None)
    address = models.TextField(default='')
    quest_type = models.CharField(max_length=50, default='CHARITY') #SPORT, CHARITY, GOV
    need_users = models.IntegerField(null=False, default=1)
    additional_bonus = models.TextField(default='') #material bonus


class Requirement(models.Model):
    gender = models.SmallIntegerField(null=True, default=None) #0 - girl, 1 - boy
    speak_english = models.BooleanField(null=True, default=None)
    min_age = models.IntegerField(null=True, default=None)
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE)
    description = models.TextField(null=True, default=None)


class Role(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True, default=None)
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE)


class UserQuest(models.Model):
    status = models.IntegerField(default=0, null=False)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE)


class UserSkills(models.Model):
    status = models.IntegerField(default=0, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
