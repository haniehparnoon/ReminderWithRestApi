from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000,default="test")
    owner = models.ForeignKey('auth.User', related_name="categories", 
    on_delete=models.CASCADE)

    def __str__(self):
        return self.category_name

class Task(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=10000,default="do somthing")
    category = models.ManyToManyField(Category)
    RATING_CHOICES = [('High','high'),('Medium','medium'),('Low','low')]
    priority = models.CharField(max_length=7,choices=RATING_CHOICES,default=3)
    STATUS_CHOICES = [('Incomplete', 'Incomplete'),('Working', 'Working'),('Done', 'Done')]
    status = models.CharField(max_length=11,choices=STATUS_CHOICES, default=1)
    create_time = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField()
    owner = models.ForeignKey('auth.User', related_name="tasks", 
    on_delete=models.CASCADE)

    def __str__(self):
        return self.title