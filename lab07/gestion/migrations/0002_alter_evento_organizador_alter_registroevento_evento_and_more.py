# Generated by Django 5.1 on 2024-10-05 20:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='organizador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eventos_organizados', to='gestion.usuario'),
        ),
        migrations.AlterField(
            model_name='registroevento',
            name='evento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registros', to='gestion.evento'),
        ),
        migrations.AlterField(
            model_name='registroevento',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registros_evento', to='gestion.usuario'),
        ),
    ]
