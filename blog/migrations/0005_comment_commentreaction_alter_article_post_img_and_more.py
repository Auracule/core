# Generated by Django 4.0.5 on 2022-08-06 10:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_article_posted_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thecomment', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('commenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommentReaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(default=False)),
                ('dislike', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='post_img',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='posted_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thereply', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('reaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.commentreaction')),
                ('replier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('thecomment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.comment')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='reaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.commentreaction'),
        ),
    ]
