# Generated by Django 4.1.3 on 2022-11-20 19:24

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
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Email', models.EmailField(max_length=254)),
                ('Subject', models.CharField(default='', max_length=200)),
                ('Message', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('sub_category', models.CharField(default='', max_length=200)),
                ('mrp', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('pub_date', models.DateField(auto_now=True)),
                ('image', models.ImageField(default='', upload_to='product_image/images')),
                ('inventory', models.IntegerField(default=1)),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Shop.category')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_time', models.DateField(auto_now=True)),
                ('review', models.CharField(default='', max_length=400)),
                ('rating', models.IntegerField(default=0)),
                ('Product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.product')),
                ('User_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
