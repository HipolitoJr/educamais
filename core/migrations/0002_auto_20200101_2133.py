# Generated by Django 2.1.3 on 2020-01-02 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prova',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota_natureza', models.FloatField(default=0.0)),
                ('nota_humanas', models.FloatField(default=0.0)),
                ('nota_matematica', models.FloatField(default=0.0)),
                ('nota_linguagens', models.FloatField(default=0.0)),
                ('nota_redacao', models.FloatField(default=0.0)),
                ('ativo', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='nota_humanas',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='nota_linguagens',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='nota_matematica',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='nota_natureza',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='nota_redacao',
        ),
        migrations.AddField(
            model_name='perfil',
            name='provas',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='provas', to='core.Prova'),
            preserve_default=False,
        ),
    ]
