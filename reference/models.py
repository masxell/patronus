from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your models here.
class Reference(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    link = models.URLField(max_length=250)
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name='reference_posts')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    #status =  models.CharField(max_length=10, choices = STATUS_CHOICES, default='draft')

    objects = models.Manager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     # return reverse('blog:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])
    #     return reverse_lazy('blog:post_detail', kwargs={'pk':self.id, 'slug':self.slug})