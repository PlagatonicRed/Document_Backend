from flask import Flask, g
from config import DATABASE
from utils.database import create_table
from routes.logging_routes import logging_bp
from routes.admin_routes import admin_bp

app = Flask(__name__)
app.config['DATABASE'] = DATABASE

# Register Blueprints
app.register_blueprint(logging_bp)
app.register_blueprint(admin_bp)

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    with app.app_context():
        create_table()
    app.run(debug=True)
