from extensions import app, db, cors
from routes.admin import admin_bp
from create_all_role_users import *

app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital.db'

db.init_app(app)
    with app.app_context():
        create_users()
cors.init_app(app)

app.register_blueprint(admin_bp)

if __name__ == "__main__":
    app.run(debug=True)
