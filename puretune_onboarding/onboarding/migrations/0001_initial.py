# Generated by Django 5.0.6 on 2024-06-09 21:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('age_group', models.CharField(choices=[('infant', 'Infant (0-1 years)'), ('toddler', 'Toddler (1-3 years)'), ('preschool', 'Preschool (3-5 years)'), ('school_age', 'School Age (6-12 years)'), ('teenager', 'Teenager (13-18 years)')], max_length=20)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('parent_type', models.CharField(blank=True, choices=[('first_time', 'First-time Parent'), ('experienced', 'Experienced Parent'), ('single', 'Single Parent'), ('adoptive', 'Adoptive Parent'), ('foster', 'Foster Parent'), ('step', 'Step Parent')], max_length=20, null=True)),
                ('link', models.URLField(max_length=500, unique=True)),
                ('snippet', models.TextField()),
                ('preview_image', models.URLField(blank=True, max_length=500, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('type', models.CharField(choices=[('blog', 'Blog'), ('vlog', 'Vlog')], default='blog', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('parent_type', models.CharField(choices=[('first_time', 'First-time Parent'), ('experienced', 'Experienced Parent'), ('single', 'Single Parent'), ('adoptive', 'Adoptive Parent'), ('foster', 'Foster Parent'), ('step', 'Step Parent')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age_group', models.CharField(choices=[('infant', 'Infant (0-1 years)'), ('toddler', 'Toddler (1-3 years)'), ('preschool', 'Preschool (3-5 years)'), ('school_age', 'School Age (6-12 years)'), ('teenager', 'Teenager (13-18 years)')], max_length=20)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='onboarding.parent')),
            ],
        ),
    ]
