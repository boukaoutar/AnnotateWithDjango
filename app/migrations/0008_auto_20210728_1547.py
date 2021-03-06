# Generated by Django 3.2.4 on 2021-07-28 13:47

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_labels'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('TREATMENT', 'Treatment'), ('DISEASE', 'Disease'), ('ANATOMY', 'Anatomy')], max_length=24)),
                ('key', models.IntegerField()),
                ('translations', jsonfield.fields.JSONField(default=dict)),
                ('position_type', models.CharField(choices=[('TOOTH', 'Tooth'), ('GENERAL', 'General'), ('NONE', 'None')], default='NONE', max_length=16)),
                ('show_on_report', models.BooleanField(default=True)),
                ('show_on_image', models.BooleanField(default=True)),
                ('show_julie', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Labels',
        ),
    ]
