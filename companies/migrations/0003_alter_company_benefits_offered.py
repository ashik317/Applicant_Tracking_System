import django.contrib.postgres.fields
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('companies', '0002_alter_companydocument_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='benefits_offered',
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    choices=[
                        ('healthcare', 'Healthcare'),
                        ('paid_time_off', 'Paid Time Off'),
                        ('retirement_plan', 'Retirement Plan'),
                        ('stock_options', 'Stock Options'),
                        ('gym_membership', 'Gym Membership'),
                        ('child_care', 'Child Care'),
                        ('paid_parents_leave', 'Paid Parental Leave'),
                        ('other', 'Other'),
                    ],
                    max_length=50,
                ),
                blank=True,
                default=list,
                size=None,
            ),
        ),
    ]
