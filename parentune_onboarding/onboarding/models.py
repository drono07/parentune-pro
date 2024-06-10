from django.db import models
import os


class Parent(models.Model):
    FIRST_TIME = "first_time"
    EXPERIENCED = "experienced"
    SINGLE = "single"
    ADOPTIVE = "adoptive"
    FOSTER = "foster"
    STEP = "step"

    PARENT_TYPE_CHOICES = [
        (FIRST_TIME, "First-time Parent"),
        (EXPERIENCED, "Experienced Parent"),
        (SINGLE, "Single Parent"),
        (ADOPTIVE, "Adoptive Parent"),
        (FOSTER, "Foster Parent"),
        (STEP, "Step Parent"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    parent_type = models.CharField(max_length=20, choices=PARENT_TYPE_CHOICES)

    def __str__(self):
        return self.name


class Child(models.Model):
    MALE = "male"
    FEMALE = "female"
    GENDER_CHOICES = [
        (MALE, "Male"),
        (FEMALE, "Female"),
    ]
    INFANT = "infant"
    TODDLER = "toddler"
    PRESCHOOL = "preschool"
    SCHOOL_AGE = "school_age"
    TEENAGER = "teenager"

    AGE_GROUP_CHOICES = [
        (INFANT, "Infant (0-1 years)"),
        (TODDLER, "Toddler (1-3 years)"),
        (PRESCHOOL, "Preschool (3-5 years)"),
        (SCHOOL_AGE, "School Age (6-12 years)"),
        (TEENAGER, "Teenager (13-18 years)"),
    ]

    parent = models.ForeignKey(
        Parent, related_name="children", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    age_group = models.CharField(max_length=20, choices=AGE_GROUP_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    def __str__(self):
        return self.name


class Blog(models.Model):
    BLOG_TYPE_CHOICES = [
        ("blog", "Blog"),
        ("vlog", "Vlog"),
    ]
    title = models.CharField(max_length=200)
    content = models.TextField()
    age_group = models.CharField(max_length=20, choices=Child.AGE_GROUP_CHOICES)
    gender = models.CharField(max_length=10, choices=Child.GENDER_CHOICES)
    parent_type = models.CharField(
        max_length=20, choices=Parent.PARENT_TYPE_CHOICES, null=True, blank=True
    )
    link = models.URLField(max_length=500, unique=True)
    snippet = models.TextField()
    preview_image = models.URLField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(
        max_length=10, choices=BLOG_TYPE_CHOICES, default="blog"
    )

    def __str__(self):
        return self.title

    class Meta:
        indexes = [
            models.Index(fields=["age_group"]),
            models.Index(fields=["gender"]),
            models.Index(fields=["parent_type"]),
        ]
