# Generated by Django 4.0 on 2025-01-27 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_profile_description_and_more'),
        ('travelp', '0006_fundraising'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customuser')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='donations', to='travelp.fundraising')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
