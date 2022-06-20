# Generated by Django 4.0.5 on 2022-06-19 10:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='nom')),
            ],
        ),
        migrations.CreateModel(
            name='DiscountCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('discount', models.FloatField(verbose_name='réduction(%)')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='date de création')),
            ],
        ),
        migrations.CreateModel(
            name='Edition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='nom')),
                ('isDLC', models.BooleanField(verbose_name='est un dlc')),
                ('price', models.FloatField(verbose_name='prix réduit(vrai prix)')),
                ('initial_price', models.FloatField(verbose_name='prix initial')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='nom')),
                ('release_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('choices_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.choices')),
            ],
            bases=('api.choices',),
        ),
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('choices_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.choices')),
            ],
            bases=('api.choices',),
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('choices_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.choices')),
            ],
            bases=('api.choices',),
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('choices_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.choices')),
            ],
            bases=('api.choices',),
        ),
        migrations.CreateModel(
            name='Support',
            fields=[
                ('choices_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.choices')),
            ],
            bases=('api.choices',),
        ),
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255, verbose_name='code')),
                ('edition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.edition', verbose_name='édition')),
            ],
        ),
        migrations.AddField(
            model_name='edition',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.game', verbose_name='jeu'),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='date de création')),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.discountcode', verbose_name='code')),
                ('editions', models.ManyToManyField(to='api.edition', verbose_name='éditions')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='utilisateur')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='developer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.developer', verbose_name='développeur'),
        ),
        migrations.AddField(
            model_name='game',
            name='editor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.editor', verbose_name='editeur'),
        ),
        migrations.AddField(
            model_name='game',
            name='genres',
            field=models.ManyToManyField(to='api.genre', verbose_name='genres'),
        ),
        migrations.AddField(
            model_name='edition',
            name='platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.platform', verbose_name='plateforme'),
        ),
    ]
