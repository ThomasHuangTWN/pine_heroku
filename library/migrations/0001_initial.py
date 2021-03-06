# Generated by Django 3.1.1 on 2020-09-29 07:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('ISBN', models.IntegerField(default=0)),
                ('date_published', models.DateField(null=True, verbose_name='date published')),
                ('summary', models.TextField()),
                ('image', models.ImageField(default='default.png', upload_to='photos/')),
            ],
        ),
        migrations.CreateModel(
            name='Borrowing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0)),
                ('date_borrowed', models.DateTimeField(null=True, verbose_name='date borrowed')),
                ('date_returned', models.DateTimeField(null=True, verbose_name='date returned')),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.book')),
                ('borrower', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='borrowed_book', to=settings.AUTH_USER_MODEL)),
                ('checkout_staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='checkouted_borrowing', to=settings.AUTH_USER_MODEL)),
                ('confirm_staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='confirmed_borrowing', to=settings.AUTH_USER_MODEL)),
                ('return_staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='returned_borrowing', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
