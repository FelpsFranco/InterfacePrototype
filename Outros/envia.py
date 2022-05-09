import smtplib
# from email.message import EmailMessage


def libera_paciente(email, name):

    nome = name
    EMAIL_ADDRESS = 'informasaida@gmail.com'
    EMAIL_PASSWORD = 'informandosaida159'

    Subject = 'Saída de Paciente'
    To = email
    TEXT = f' {nome} Paciente Liberado de Seu Leito'

    server = smtplib.SMTP('smtp.gmail.com', 465)
    server.ehlo()
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    BODY = '\r\n'.join(['To: %s' % To,
                        'From: %s' % EMAIL_ADDRESS,
                        'Subject: %s' % Subject,
                        '', TEXT])

    server.sendmail(EMAIL_ADDRESS, [To], BODY)

    # with smtplib.SMTP_SSL('smtp.gmail.com', 587) as smtp:
    #     smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    #     smtp.send_message(msg)
