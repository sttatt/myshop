# Generated by Django 2.2.2 on 2019-06-15 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_tempproduct_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('PROCCESING', 'В обработке'), ('SHIPMENT', 'Отправлен'), ('CLOSED', 'Закрыт')], max_length=20, null=True),
        ),
    ]
