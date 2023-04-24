from flask import Blueprint, jsonify, request
from werkzeug.exceptions import BadRequest, NotFound
from datetime import datetime

from .db import get_db

bp = Blueprint("student", __name__, url_prefix="/api")

@bp.route("/students", methods=["GET"])
def get_students():
    db = get_db()
    students = db.execute(
        "SELECT * FROM student"
    ).fetchall()
    return jsonify(students)

@bp.route("/students/<int:id>", methods=["GET"])
def get_student(id):
    db = get_db()
    student = db.execute(
        "SELECT * FROM student WHERE id = ?", (id,)
    ).fetchone()
    if student is None:
        raise NotFound(f"Student with id {id} not found")
    return jsonify(student)

@bp.route("/students", methods=["POST"])
def create_student():
    db = get_db()
    data = request.get_json()
    if not data:
        raise BadRequest("No input data provided")
    name = data.get("name")
    surname = data.get("surname")
    email = data.get("email")
    date_of_birth = data.get("date_of_birth")
    gender = data.get("gender")
    major = data.get("major")
    if not name or not surname or not email or not date_of_birth or not gender or not major:
        raise BadRequest("Missing required fields")

    try:
        date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")
    except ValueError:
        raise BadRequest("Invalid date format. Should be YYYY-MM-DD")

    db.execute(
        "INSERT INTO student (name, surname, email, date_of_birth, gender, major) VALUES (?, ?, ?, ?, ?, ?)",
        (name, surname, email, date_of_birth, gender, major),
    )
    db.commit()
    return "", 201

@bp.route("/students/<int:id>", methods=["PUT"])
def update_student(id):
    db = get_db()
    data = request.get_json()
    if not data:
        raise BadRequest("No input data provided")
    name = data.get("name")
    surname = data.get("surname")
    email = data.get("email")
    date_of_birth = data.get("date_of_birth")
    gender = data.get("gender")
    major = data.get("major")
    if not name or not surname or not email or not date_of_birth or not gender or not major:
        raise BadRequest("Missing required fields")

    try:
        date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")
    except ValueError:
        raise BadRequest("Invalid date format. Should be YYYY-MM-DD")

    student = db.execute(
        "SELECT * FROM student WHERE id = ?", (id,)
    ).fetchone()
    if student is None:
        raise NotFound(f"Student with id {id} not found")

    db.execute(
        "UPDATE student SET name = ?, surname = ?, email = ?, date_of_birth = ?, gender = ?, major = ? WHERE id = ?",
        (name, surname, email, date_of_birth, gender, major, id),
    )
    db.commit()
    return "", 204

@bp.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    db = get_db()
    student = db.execute(
        "SELECT * FROM student WHERE id = ?", (id,)
    ).fetchone()
    if student is None:
        raise NotFound(f"Student with id {id} not found")
    db.execute("DELETE FROM student WHERE id = ?", (id,))
    db.commit()
    return "", 204
