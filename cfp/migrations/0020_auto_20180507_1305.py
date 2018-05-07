# Generated by Django 2.0.4 on 2018-05-07 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfp', '0019_auto_20180507_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='paperapplication',
            name='travel_expenses_required',
            field=models.BooleanField(default=False, help_text='For people outside of the Zagreb area, we provide up to €200 in travel expenses.', verbose_name='I require travel expenses'),
        ),
        migrations.AlterField(
            model_name='paperapplication',
            name='accomodation_required',
            field=models.BooleanField(default=False, help_text='For people outside of the Zagreb area, we provide 3 nights in an apartment.', verbose_name='I require accommodation'),
        ),
    ]
