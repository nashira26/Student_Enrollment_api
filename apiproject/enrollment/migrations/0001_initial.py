# Generated by Django 4.2.3 on 2023-07-05 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FunnelStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('status', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='enrollment.funnelstatus')),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('status_after', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs_after', to='enrollment.funnelstatus')),
                ('status_before', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs_before', to='enrollment.funnelstatus')),
                ('student_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enrollment.student')),
            ],
        ),
    ]
