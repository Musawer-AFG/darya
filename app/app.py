from flask import Flask, abort

app = Flask(__name__, template_folder="views")
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'