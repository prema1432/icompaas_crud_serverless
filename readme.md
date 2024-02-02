# Initialization
flask db init

# Generate a migration
flask db migrate -m "Initial migration"

# Apply the migration
flask db upgrade


# run server
flask run --port 3005

# pre commit install
brew install pre-commit \
pip install pre-commit\
pre-commit install\
pre-commit run --all-files
