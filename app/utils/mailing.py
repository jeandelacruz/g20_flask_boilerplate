from os import getenv
from app import mail
from flask import render_template
from flask_mail import Message


class Mailing:
    def __init__(self):
        self.sender = ('Flask Boilerplate', getenv('MAIL_USERNAME'))

    def mail_reset_password(self, name, recipient, new_password):
        html = render_template('reset_password.html',
                               name_complete=name, password=new_password)
        return self.__send_mail(
            f'Reinicio de contraseña - {recipient}',
            [recipient],
            html
        )

    def __send_mail(self, subject, recipients, html):
        message = Message(
            subject=subject,
            sender=self.sender,
            recipients=recipients,
            html=html
        )
        return mail.send(message)
