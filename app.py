from flask import Flask, render_template, request, redirect, url_for

import mysql.connector

app = Flask(__name__)
encryption_key = 'key'
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

@app.route("/studentsList")
def studentsList():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""
    SELECT student.id, student.full_name, student.course,
    CAST(AES_DECRYPT(student.phone, 'key') AS CHAR) AS phone,
    discipline.name AS discipline_name
    FROM student
    JOIN discipline ON student.discipline_id = discipline.id
""")

    students = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('studentsList.html', students=students)


@app.route("/addStudent", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        full_name = request.form['full_name']
        course = request.form['course']
        phone = request.form['phone']
        discipline_id = request.form['discipline_id']

        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(f"""
            INSERT INTO student (full_name, course, phone, discipline_id)
            VALUES (%s, %s, AES_ENCRYPT(%s, '{encryption_key}'), %s)
        """, (full_name, course, phone, discipline_id))
        connection.commit()
        cursor.close()
        connection.close()
        return redirect(url_for('studentsList'))

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
