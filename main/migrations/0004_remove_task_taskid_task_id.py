# Generated by Django 5.1 on 2024-08-22 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_task_tasklistid_task_userid_delete_tasklist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='taskid',
        ),
        migrations.AddField(
            model_name='task',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
