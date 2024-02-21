# Generated by Django 4.2.6 on 2023-10-30 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familydetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family_values', models.CharField(max_length=150)),
                ('family_type', models.CharField(max_length=150)),
                ('family_status', models.CharField(max_length=150)),
                ('no_of_brothers', models.CharField(default='null', max_length=150)),
                ('no_of_brothers_married', models.CharField(default='null', max_length=150)),
                ('no_of_sisters', models.CharField(default='null', max_length=150)),
                ('no_of_sisters_married', models.CharField(default='null', max_length=150)),
                ('mother_tounge', models.CharField(max_length=150)),
                ('father_name', models.CharField(default='null', max_length=150)),
                ('father_occupation', models.CharField(default='null', max_length=150)),
                ('mother_name', models.CharField(default='null', max_length=150)),
                ('mother_occupation', models.CharField(default='null', max_length=150)),
                ('family_wealth', models.CharField(default='null', max_length=150)),
                ('about_family', models.CharField(max_length=150)),
                ('options', models.CharField(choices=[('My parents will stay with me after marriage', 'My parents will stay with me after marriage'), ('My parents will not stay with me after marriage', 'My parents will not stay with me after marriage'), ('Dont wish to specify', 'Dont wish to specify')], max_length=255)),
            ],
        ),
    ]
