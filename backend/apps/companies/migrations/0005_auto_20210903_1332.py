# Generated by Django 3.2.7 on 2021-09-03 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_company_partners'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='partners',
        ),
        migrations.AddField(
            model_name='company',
            name='partners_companies',
            field=models.ManyToManyField(blank=True, related_name='_companies_company_partners_companies_+', to='companies.Company', verbose_name='Партнеры'),
        ),
    ]
