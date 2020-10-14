# Generated by Django 3.1.1 on 2020-10-11 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=24, verbose_name='사용자명')),
                ('password', models.CharField(max_length=200, verbose_name='비밀번호')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='이름')),
                ('birth', models.CharField(max_length=10, null=True, verbose_name='생년월일')),
                ('email', models.CharField(max_length=50, null=True, verbose_name='이메일')),
                ('phone_num', models.CharField(max_length=15, null=True, verbose_name='휴대폰번호')),
                ('addr', models.CharField(max_length=50, null=True, verbose_name='주소')),
                ('rcmd_id', models.CharField(max_length=24, null=True, verbose_name='추천인아이디')),
                ('is_expert', models.CharField(default='', max_length=10, verbose_name='전문가여부')),
                ('registered_dttm', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
            ],
        ),
    ]
