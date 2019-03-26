# Generated by Django 2.1.7 on 2019-03-17 10:35

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Compound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', django.contrib.postgres.fields.jsonb.JSONField(default={'ccdc': '', 'dimensionality': 0, 'formula': '', 'ueff': ''})),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doi', models.CharField(max_length=200, unique=True, verbose_name='DOI')),
                ('info', django.contrib.postgres.fields.jsonb.JSONField(default={'authors': [], 'journal': '', 'month': '', 'pub_name': '', 'year': ''})),
                ('submitter', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='compound',
            name='doi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='datastore.Reference'),
        ),
        migrations.AddField(
            model_name='compound',
            name='submitter',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
