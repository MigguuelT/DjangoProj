# Generated by Django 4.2.21 on 2025-05-27 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('message', models.TextField(verbose_name='Mensagem')),
                ('submitted_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Submissão')),
            ],
            options={
                'verbose_name': 'Submissão de Contato',
                'verbose_name_plural': 'Submissões de Contato',
                'ordering': ['-submitted_at'],
            },
        ),
    ]
