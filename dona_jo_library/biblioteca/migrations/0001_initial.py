
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField()),
                ('description', models.CharField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField()),
                ('description', models.CharField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Status',
                'verbose_name_plural': 'Statuses',
            },
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('ean_isbn13', models.CharField(blank=True, max_length=13)),
                ('upc_isbn10', models.CharField(blank=True, max_length=10)),
                ('author_first_name', models.CharField(blank=True, max_length=100)),
                ('author_last_name', models.CharField(blank=True, max_length=100)),
                ('publisher', models.CharField(blank=True, max_length=255)),
                ('description', models.CharField(blank=True, max_length=700)),
                ('year', models.CharField(blank=True, max_length=10)),
                ('rating', models.CharField(blank=True, max_length=50)),
                ('item_type', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='genre', to='biblioteca.genres')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='status', to='biblioteca.status')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
        migrations.CreateModel(
            name='Loans',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=100)),
                ('loan_date', models.DateTimeField()),
                ('return_date', models.DateTimeField(blank=True, null=True)),
                ('expected_return_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='loans', to='biblioteca.books')),
                ('loaner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='loaner_loans', to=settings.AUTH_USER_MODEL)),
                ('renter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='renter_loans', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Loan',
                'verbose_name_plural': 'Loans',
            },
        ),
    ]
