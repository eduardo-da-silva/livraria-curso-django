# Generated by Django 3.2.7 on 2021-10-29 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_itenscompra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itenscompra',
            name='livro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='livros', to='core.livro'),
        ),
    ]
