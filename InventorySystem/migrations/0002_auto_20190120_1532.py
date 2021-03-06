# Generated by Django 2.1.5 on 2019-01-20 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('InventorySystem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='materialtype',
            name='sell_unit',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='sell_unit', to='InventorySystem.UnitLookup'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='materialtype',
            name='buy_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buy_unit', to='InventorySystem.UnitLookup'),
        ),
    ]
