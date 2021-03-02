from flask import Flask
from auth.auth import auth_bp

app = Flask(__name__)
app.config.from_object('config.ProductionConfig')
app.register_blueprint(auth_bp, url_prefix='/auth')

if __name__ == '__main__':
    app.run()
