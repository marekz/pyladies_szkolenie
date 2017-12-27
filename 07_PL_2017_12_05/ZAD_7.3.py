# Napisz program, który: po wejściu na adres /user/<username>/set-password
# ustawi hasło użytkownika username (na podstawie podanego JSON-a).

from flask import Flask, request

app = Flask(__name__)

