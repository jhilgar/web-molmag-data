# Generated by Django 2.1.5 on 2019-03-17 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_author', models.CharField(max_length=100)),
                ('institution', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['primary_author', 'institution'],
            },
        ),
        migrations.CreateModel(
            name='Dimension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the dimensionality of the magnet (e.g. 0(molecular), linear chain(1D), etc.)', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Magnet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('compound', models.CharField(max_length=256)),
                ('Ueffective', models.CharField(help_text='Enter the effective barrier height in wavenumbers', max_length=12)),
                ('doi', models.CharField(help_text='DOI from the original publication', max_length=48, verbose_name='DOI')),
                ('csdd', models.CharField(help_text='Cambridge Crystallographic structural database number (CCDC) from the original publication - if applicable', max_length=48, verbose_name='CCDC')),
                ('date_of_publication', models.DateField(blank=True, null=True)),
                ('author', models.ManyToManyField(help_text='Select an author for this magnet.', to='datastore.Author')),
                ('dimension', models.ManyToManyField(help_text='Select a dimensionality for this magnet.', to='datastore.Dimension')),
            ],
        ),
    ]
