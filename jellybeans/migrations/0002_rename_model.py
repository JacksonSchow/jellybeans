from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('jellybeans', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='JellybeanFlavors',
            new_name='JellybeanFlavor',
        ),
    ]
