# Generated by Django 2.1.2 on 2019-01-22 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makam', '0004_recording_has_lyrics'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artist',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='composer',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='form',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='instrument',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='makam',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='recording',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='release',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='symbtr',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='usul',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='work',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='artist',
            name='artist_type',
            field=models.CharField(choices=[('P', 'Person'), ('G', 'Group')], default='P', max_length=1),
        ),
        migrations.AlterField(
            model_name='artist',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='composer',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True),
        ),
    ]