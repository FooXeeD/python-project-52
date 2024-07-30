# Generated by Django 5.0.7 on 2024-07-29 10:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('labels', '0001_initial'),
        ('statuses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('name', models.CharField(
                    max_length=150,
                    unique=True,
                    verbose_name='Name')),
                ('description', models.TextField(
                    blank=True,
                    max_length=10000,
                    verbose_name='Description')),
                ('date_created', models.DateTimeField(
                    auto_now_add=True,
                    verbose_name='Creation date')),
                ('author', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name='author',
                    to=settings.AUTH_USER_MODEL,
                    verbose_name='Author')),
                ('executor', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name='executor',
                    to=settings.AUTH_USER_MODEL,
                    verbose_name='Executor')),
                ('status', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name='statuses',
                    to='statuses.status',
                    verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
            },
        ),
        migrations.CreateModel(
            name='TaskLabelRelation',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('label', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    to='labels.label')),
                ('task', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='tasks.task')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='labels',
            field=models.ManyToManyField(
                blank=True,
                related_name='labels',
                through='tasks.TaskLabelRelation',
                to='labels.label',
                verbose_name='Labels'),
        ),
    ]