from flask import Flask

new = Flask(__name__)

@new.route('/')
def my_name():
    return 'Annekah'