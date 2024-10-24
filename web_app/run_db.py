from app import app, db

# Создание всех таблиц
with app.app_context():
    db.create_all()

print("Таблицы успешно созданы!")
