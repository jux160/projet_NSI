import os

secret_key = "m^iahr((ghy)+_-l#p(o%cmx&g#jbr%6l@*_(6nniwlco#7@+o"

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite://'+ os.path.join(basedir, 'app.db')