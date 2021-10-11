# Generated by Django 3.2.8 on 2021-10-10 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('librarybooks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank='true', max_length=100, null='true')),
                ('author_name', models.CharField(blank='true', max_length=50, null='true')),
                ('isbn_num', models.CharField(blank='true', max_length=50, null='true')),
                ('genre', models.CharField(blank='true', max_length=50, null='true')),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
        migrations.CreateModel(
            name='library_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank='true', max_length=100, null='true')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='library_book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='librarybooks.book')),
                ('library', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='librarybooks.library')),
            ],
            options={
                'verbose_name': 'Library Book',
                'verbose_name_plural': 'Library Books',
            },
        ),
        migrations.CreateModel(
            name='library_activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_type', models.CharField(blank=True, choices=[('checked_in', 'checked_in'), ('checked_out', 'checked_out')], default='checked_in', max_length=255, null=True)),
                ('checked_out_at', models.DateTimeField(blank=True, null=True)),
                ('checked_in_at', models.DateTimeField(blank=True, null=True)),
                ('library_book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='librarybooks.library_book')),
                ('library_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='librarybooks.library_user')),
            ],
            options={
                'verbose_name': 'Library activity',
                'verbose_name_plural': 'Library activities',
            },
        ),
    ]
