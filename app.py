from . import app, db
from flask import request, make_response
from .models import Users, Funds
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import datetime, timedelta

@app.route("/signup", methods=["POST"])
def signup():
    data = request.json
    email = data.get("email")
    firstName = data.get("firstName")
    lastName = data.get("lastName")
    password = data.get("password")

    if firstName and lastName and email and password:
        user = Users.query.filter_by(email=email).first()
        if user:
            return make_response(
                {"message": "An account with this email already exists, please sign in"},
                200
            )
        user = Users(
            email = email,
            password = generate_password_hash(password),
            firstName = firstName,
            lastName = lastName
        )
        db.session.add(user)
        db.session.commit()
        return make_response(
            {"message": "User created!"},
            201
        )
    return make_response(
        {"message": "Unable to create User"},
        500
    )

@app.route("/login", methods=["POST"])
def login():
    auth = request.json
    if not auth or not auth.get("email") or not auth.get("password"):
        return make_response(
            {"message": "Incorrect credentials were provided, please try again"},
            401
        )
    user = Users.query.filter_by(email = auth.get("email")).first()
    if not user: 
        return make_response(
            {"message":"Please create an account"},
            401
        )
    if check_password_hash(user.password, auth.get("password")):
        token = jwt.decode({
            'id': user.id,
            'exp': datetime.utcnow + timedelta(minutes=30)
        },
        "secret",
        "HS256"
        )
        return make_response({'token':token}, 201)
    return make_response(
        'Please check your credentials',
        401
    )



