import smtplib


def libera_paciente(email, name, data):
    EMAIL_ADDRESS = 'informasaida@gmail.com'
    EMAIL_PASSWORD = 'informandosaida159'
    email_envio = (email[0][0])
    nome_envio = (name[0][0])
    subject = 'Paciente Liberado de Seu Leito:'
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    server.sendmail(EMAIL_ADDRESS, email_envio, nome_envio)
    print('Email enviado')

    server.quit()
