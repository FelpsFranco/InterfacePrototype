import datetime
import smtplib
from email.message import EmailMessage


def libera_paciente():

    EMAIL_ADDRESS = 'informasaida@gmail.com'
    EMAIL_PASSWORD = 'informandosaida159'

    msg = EmailMessage()
    msg['Subject'] = 'Saída de Paciente'
    msg['From'] = 'informasaida@gmail.com'
    msg['To'] = 'felipefranco.morg@outlook.com'
    msg.set_content('Paciente Liberado de Seu Leito')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

