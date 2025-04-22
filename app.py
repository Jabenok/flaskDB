from flask import Flask, render_template, request, redirect, url_for, session

import mysql.connector

app = Flask(__name__)
encryption_key = 'key'
app.secret_key = 'key2'
@app.route("/")
def index():
    return render_template('index.html')

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='universitydb'
    )
    return connection

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login = request.form["login"]
        password = request.form["password"]

        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("""
            SELECT id, login, role
            FROM users
            WHERE login = %s AND password = AES_ENCRYPT(%s, %s)
        """, (login, password, encryption_key))

        user = cursor.fetchone()
        cursor.close()
        connection.close()

        if user:
            # Сохраняем данные в сессии
            session["user_id"] = user["id"]
            session["login"] = user["login"]
            session["role"] = user["role"]
            return redirect(url_for("studentsList"))
        else:
            return render_template("login.html", error="Неверный логин или пароль")

    return render_template("login.html")




@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        login_value = request.form["login"]
        password = request.form["password"]
        role = request.form["role"]

        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT id FROM users WHERE login = %s", (login_value,))
        existing_user = cursor.fetchone()

        if existing_user:
            cursor.close()
            connection.close()
            return render_template("register.html", error="Пользователь с таким логином уже существует")

        cursor.execute("""
            INSERT INTO users (login, password, role)
            VALUES (%s, AES_ENCRYPT(%s, %s), %s)
        """, (login_value, password, encryption_key, role))

        connection.commit()
        cursor.close()
        connection.close()

        return render_template("register.html", message="Регистрация прошла успешно")

    return render_template("register.html")



@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/studentsList")
def studentsList():
    # Проверка на наличие роли в сессии
    if "role" not in session:
        return redirect(url_for('login'))  # Перенаправляем на страницу входа, если роль не в сессии

    role = session["role"]

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    if role == 'teacher':
        # Преподаватель видит все данные, включая расшифрованный номер телефона
        cursor.execute("""
            SELECT student.id, student.full_name, student.course,
            CAST(AES_DECRYPT(student.phone, %s) AS CHAR) AS phone,
            discipline.name AS discipline_name
            FROM student
            JOIN discipline ON student.discipline_id = discipline.id
        """, (encryption_key,))
    elif role == 'student':
        # Студент видит только свой телефон, остальные скрыты
        cursor.execute("""
            SELECT student.id, student.full_name, student.course,
            CASE WHEN student.id = %s THEN
                CAST(AES_DECRYPT(student.phone, %s) AS CHAR)
            ELSE 'скрыто' END AS phone,
            discipline.name AS discipline_name
            FROM student
            JOIN discipline ON student.discipline_id = discipline.id
        """, (session["user_id"], encryption_key))  # Используем user_id из сессии
    else:
        return "Нет доступа", 403

    students = cursor.fetchall()
    cursor.close()
    connection.close()

    return render_template('studentsList.html', students=students)





@app.route("/addStudent", methods=["GET", "POST"])
def add_student():
    # Проверяем роль пользователя из сессии
    if "role" not in session:
        return redirect(url_for('login'))  # Перенаправляем на страницу входа, если роль не найдена

    role = session["role"]  # Получаем роль из сессии

    # Проверяем, если роль не 'teacher', перенаправляем на страницу с ошибкой или список студентов
    if role != 'teacher':
        return redirect(url_for('studentsList'))  # Или можешь вернуть страницу с ошибкой

    if request.method == "POST":
        full_name = request.form['full_name']
        course = request.form['course']
        phone = request.form['phone']
        discipline_id = request.form['discipline_id']

        # Соединение с БД и добавление студента
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(f"""
            INSERT INTO student (full_name, course, phone, discipline_id)
            VALUES (%s, %s, AES_ENCRYPT(%s, '{encryption_key}'), %s)
        """, (full_name, course, phone, discipline_id))
        connection.commit()
        cursor.close()
        connection.close()

        return redirect(url_for('studentsList'))  # Перенаправление на список студентов после добавления

    # Получаем список дисциплин, если пользователь teacher
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM discipline")
    disciplines = cursor.fetchall()
    cursor.close()
    connection.close()

    return render_template('addStudent.html', disciplines=disciplines)


@app.route("/deleteStudent/<int:id>")
def delete_student(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM student WHERE id = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('studentsList'))


@app.route("/editStudent/<int:student_id>", methods=["GET", "POST"])
def edit_student(student_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # Получаем данные студента, включая расшифрованный телефон
    cursor.execute("""
        SELECT student.*, CAST(AES_DECRYPT(student.phone, %s) AS CHAR) AS phone
        FROM student
        WHERE id = %s
    """, (encryption_key, student_id))
    
    student = cursor.fetchone()

    # Если студент не найден, перенаправляем на список студентов
    if not student:
        return redirect(url_for('studentsList'))

    # Получаем список дисциплин для выбора
    cursor.execute("SELECT * FROM discipline")
    disciplines = cursor.fetchall()
    cursor.close()

    if request.method == "POST":
        # Получаем данные из формы
        full_name = request.form['full_name']
        course = request.form['course']
        phone = request.form['phone']
        discipline_id = request.form['discipline_id']

        # Обновляем данные студента
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE student
            SET full_name = %s, course = %s, phone = AES_ENCRYPT(%s, %s), discipline_id = %s
            WHERE id = %s
        """, (full_name, course, phone, encryption_key, discipline_id, student_id))
        connection.commit()
        cursor.close()
        connection.close()

        return redirect(url_for('studentsList'))

    return render_template('editStudent.html', student=student, disciplines=disciplines)



if __name__ == '__main__':
    app.run(debug=True)
