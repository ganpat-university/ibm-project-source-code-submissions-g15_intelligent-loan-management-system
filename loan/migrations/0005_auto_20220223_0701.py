# Generated by Django 3.0.7 on 2022-02-23 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
        ('loan', '0004_question'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Policy',
            new_name='Loan',
        ),
        migrations.RenameModel(
            old_name='PolicyRecord',
            new_name='LoanRecord',
        ),
        migrations.RenameField(
            model_name='loan',
            old_name='policy_name',
            new_name='loan_name',
        ),
        migrations.RenameField(
            model_name='loanrecord',
            old_name='Policy',
            new_name='Loan',
        ),
    ]
