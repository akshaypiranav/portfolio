# Generated by Django 4.2.1 on 2024-01-06 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0002_rename_description_projects_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResumeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume_file', models.FileField(upload_to='resume_files/')),
            ],
        ),
    ]
