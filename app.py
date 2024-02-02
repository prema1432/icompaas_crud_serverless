import awsgi
from app import app

if __name__ == "__main__":
    app.run()


def lambda_handler(event, context):
    return awsgi.response(app, event, context, base64_content_types={"image/png"})
