# Generated by Django 4.2 on 2023-05-11 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0019_alter_user_first_name_jobapplication'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscription_type', models.CharField(max_length=20)),
                ('duration_in_days', models.IntegerField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.AlterField(
            model_name='company',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='jobposting',
            name='description',
            field=models.TextField(max_length=800),
        ),
        migrations.AlterField(
            model_name='jobposting',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='jobposting',
            name='qualifications',
            field=models.TextField(max_length=800),
        ),
        migrations.AlterField(
            model_name='jobposting',
            name='requirements',
            field=models.TextField(max_length=800),
        ),
        migrations.AlterField(
            model_name='jobposting',
            name='responsibilities',
            field=models.TextField(max_length=800),
        ),
    ]