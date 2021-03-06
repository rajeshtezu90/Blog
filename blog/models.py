from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.


class CommonField(models.Model):
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


class Post(CommonField):
    title = models.CharField(max_length=200)
    #author = models.ForeignKey('auth.User')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class Comment(CommonField):
    post = models.ForeignKey('blog.Post', related_name='comments')
    # author = models.CharField(max_length=200)
    author = models.ForeignKey(User)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text
