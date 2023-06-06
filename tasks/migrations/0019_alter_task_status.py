# Generated by Django 4.1.7 on 2023-06-05 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0018_alter_task_status_alter_usernotification_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('ON HOLD', 'On Hold'), ('IN PROGRESS', 'In Progress'), ('COMPLETED', 'Completed')], default='ON HOLD', max_length=20),
        ),
    ]
