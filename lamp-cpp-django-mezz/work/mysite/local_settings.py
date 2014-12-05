
DEBUG = False

# Make these unique, and don't share it with anybody.
SECRET_KEY = "7d9d5c9c-336f-49fb-bb2d-3d56ffba42b37a1a071d-c32a-4923-b422-6f752264bd5a6a142c40-6c5e-4a4f-98d1-3a1a1c28a785"
NEVERCACHE_KEY = "48136500-4a3c-4ace-b344-c43b304d612e8f2cdc6f-f894-43d3-992c-b00fb7b79cd4d52a4a15-8446-4677-a85e-8630a2eb9e50"

DATABASES = {
    "default": {
        # Add "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.mysql",
        # DB name or path to database file if using sqlite3.
        "NAME": "my_db_name",
        # Not used with sqlite3.
        "USER": "my_user_name",
        # Not used with sqlite3.
        "PASSWORD": "my_mysql_user_password",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "localhost",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "3306",
    }
}
