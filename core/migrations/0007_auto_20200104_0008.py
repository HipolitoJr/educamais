# Generated by Django 2.1.3 on 2020-01-04 03:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_escola_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='escola',
            name='usuario',
        ),
        migrations.AlterField(
            model_name='perfil',
            name='escola',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alunos', to='administracao.Escola'),
        ),
        migrations.DeleteModel(
            name='Escola',
        ),
    ]
