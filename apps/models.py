# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

DELETED = 1
NOT_DELETED = 0

DELETED_STATUS = (
    (NOT_DELETED, "Not Deleted"),
    (DELETED, "Deleted")
)


class Anger(models.Model):

    level = models.CharField(max_length=10)
    color = models.CharField(max_length=10, null=True)
    deleted = models.IntegerField(
        choices=DELETED_STATUS, default=NOT_DELETED
    )
    created_at = models.DateTimeField(null=False)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        if self.created_at is None:
            self.created_at = timezone.now()
        else:
            self.updated_at = timezone.now()

    def __str__(self, *args, **kwargs):
        return '{}'.format(self.level)


class Post(models.Model):
    user = models.ForeignKey(User, db_column='user')
    anger = models.ForeignKey(Anger, related_name='anger_level')
    description = models.CharField(max_length=255)
    deleted = models.IntegerField(
        choices=DELETED_STATUS, default=NOT_DELETED
    )
    created_at = models.DateTimeField(null=False)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        ordering = ["-created_at", "-updated_at"]

    def save(self, *args, **kwargs):
        if self.created_at is None:
            self.created_at = timezone.now()
        else:
            self.updated_at = timezone.now()
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return 'User {}, anger level: {}'.format(self.user, self.anger)
