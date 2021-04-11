# Generated by Django 3.1.7 on 2021-04-08 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appix', '0002_inlinechoicexcard'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagecard',
            old_name='subjectName',
            new_name='subject',
        ),
        migrations.RenameField(
            model_name='imagecard',
            old_name='linkedTopic',
            new_name='tag',
        ),
        migrations.RenameField(
            model_name='inlineimagexcard',
            old_name='images',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='multiplechoicecard',
            old_name='subjectName',
            new_name='subject',
        ),
        migrations.RenameField(
            model_name='multiplechoicecard',
            old_name='linkedTopic',
            new_name='tag',
        ),
        migrations.RenameField(
            model_name='simplecard',
            old_name='subjectName',
            new_name='subject',
        ),
        migrations.RenameField(
            model_name='simplecard',
            old_name='linkedTopic',
            new_name='tag',
        ),
        migrations.RemoveField(
            model_name='imagecard',
            name='concept',
        ),
        migrations.RemoveField(
            model_name='multiplechoicecard',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='multiplechoicecard',
            name='concept',
        ),
        migrations.RemoveField(
            model_name='simplecard',
            name='concept',
        ),
        migrations.AlterField(
            model_name='imagecard',
            name='counter',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='multiplechoicecard',
            name='counter',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='simplecard',
            name='answer',
            field=models.TextField(default='Write here your answer...'),
        ),
        migrations.AlterField(
            model_name='simplecard',
            name='counter',
            field=models.IntegerField(default=0),
        ),
    ]