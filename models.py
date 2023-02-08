from django.db import models

#Create your models here.
LIKE_CHOICES = (
    ('OUI', 'OUI'),
    ('NON', 'NON'),
)
class Subject(models.Model):
    name = models.CharField(max_length=100, blank=True)
    code = models.CharField(max_length=50, blank=True)
    Year = models.CharField(max_length=100, blank=True)
    Semester = models.CharField(max_length=100, blank=True)
    Lec_name = models.CharField(max_length=100, blank=True)
    Sequence = models.CharField(max_length=50, blank=True)
    Group = models.CharField(max_length=50, blank=True)
    info = models.CharField(max_length=100, blank=True)
    quiz = models.CharField(max_length=150, blank=True)
    obt_no = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    Total_no = models.IntegerField(default=5, null=True, blank=True)

    quiz1 = models.CharField(max_length=150, blank=True)
    obt_no1 = models.IntegerField(default=0, null=True, blank=True)
    Total_no1 = models.IntegerField(default=5, null=True, blank=True)

    quiz2 = models.CharField(max_length=150, blank=True)
    obt_no2 = models.IntegerField(default=0, null=True, blank=True)
    Total_no2 = models.IntegerField(default=5, null=True, blank=True)

    Value_name = models.CharField(max_length=100, blank=True)
    value = models.CharField(choices=LIKE_CHOICES, default='OUI', max_length=100)

    quiz3 = models.CharField(max_length=150, blank=True)
    obt_no3 = models.IntegerField(default=0, null=True, blank=True)
    Total_no3 = models.IntegerField(default=5, null=True, blank=True)

    quiz4 = models.CharField(max_length=150, blank=True)
    obt_no4 = models.IntegerField(default=0, null=True, blank=True)
    Total_no4 = models.IntegerField(default=5, null=True, blank=True)

    quiz5 = models.CharField(max_length=150, blank=True)
    obt_no5 = models.IntegerField(default=0, null=True, blank=True)
    Total_no5 = models.IntegerField(default=5, null=True, blank=True)

    quiz6 = models.CharField(max_length=150, blank=True)
    obt_no6 = models.IntegerField(default=0, null=True, blank=True)
    Total_no6 = models.IntegerField(default=5, null=True, blank=True)

    quiz7 = models.CharField(max_length=150, blank=True)
    obt_no7 = models.IntegerField(default=0, null=True, blank=True)
    Total_no7 = models.IntegerField(default=5, null=True, blank=True)

    Value_name1 = models.CharField(max_length=100, blank=True)
    value1 = models.CharField(choices=LIKE_CHOICES, default='OUI', max_length=100)

    quiz8 = models.CharField(max_length=150, blank=True)
    obt_no8 = models.IntegerField(default=0, null=True, blank=True)
    Total_no8 = models.IntegerField(default=5, null=True, blank=True)

    quiz9 = models.CharField(max_length=150, blank=True)
    obt_no9 = models.IntegerField(default=0, null=True, blank=True)
    Total_no9 = models.IntegerField(default=5, null=True, blank=True)

    quiz10 = models.CharField(max_length=150, blank=True)
    obt_no10 = models.IntegerField(default=0, null=True, blank=True)
    Total_no10 = models.IntegerField(default=5, null=True, blank=True)

    quiz11 = models.CharField(max_length=150, blank=True)
    obt_no11 = models.IntegerField(default=0, null=True, blank=True)
    Total_no11 = models.IntegerField(default=5, null=True, blank=True)

    quiz12 = models.CharField(max_length=150, blank=True)
    obt_no12 = models.IntegerField(default=0, null=True, blank=True)
    Total_no12 = models.IntegerField(default=5, null=True, blank=True)

    quiz13 = models.CharField(max_length=150, blank=True)
    obt_no13 = models.IntegerField(default=0, null=True, blank=True)
    Total_no13 = models.IntegerField(default=5, null=True, blank=True)

    Value_name2 = models.CharField(max_length=100, blank=True)
    value2 = models.CharField(choices=LIKE_CHOICES, default='OUI', max_length=100)

    quiz14 = models.CharField(max_length=150, blank=True)
    obt_no14 = models.IntegerField(default=0, null=True, blank=True)
    Total_no14 = models.IntegerField(default=5, null=True, blank=True)

    quiz15 = models.CharField(max_length=150, blank=True)
    obt_no15 = models.IntegerField(default=0, null=True, blank=True)
    Total_no15 = models.IntegerField(default=5, null=True, blank=True)

    def __str__(self):
        return self.name
class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)