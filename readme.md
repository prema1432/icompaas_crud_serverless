# Initialization
flask db init

# Generate a migration
flask db migrate -m "Initial migration"

# Apply the migration
flask db upgrade


# run server
flask run --port 3005
