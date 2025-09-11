from django.db import migrations

def update_phone_column(apps, schema_editor):
    User = apps.get_model('users', 'User')
    User.objects.filter(phone__isnull=True).update(phone='Unknown')

class Migration(migrations.Migration):
    dependencies = [
        ('users', '0004_set_default_phone'),
    ]

    operations = [
        migrations.RunPython(update_phone_column),
    ]