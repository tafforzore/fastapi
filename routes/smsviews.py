import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import uuid



def send_Email(destinataire, sujet, corps_message):
    message_id = str(uuid.uuid4())
    expediteur = 'bobymomo6@genesis-compagnie.go.yj.fr'

    message = MIMEMultipart()
    message['From'] = expediteur
    message['To'] = destinataire
    message['Subject'] = sujet
    message['Message-ID'] = f'<{message_id}@tandisgicaedef.cm>' 

    message.attach(MIMEText(corps_message, 'plain'))

    try:
        serveur_smtp = 'https://node160-eu.n0c.com'
        port_smtp = 465
        mot_de_passe = 'y*Dy8Q+.W8l888Ty8'

        server = smtplib.SMTP_SSL(serveur_smtp, port_smtp)
        server.login(expediteur, mot_de_passe)
        server.sendmail(expediteur, destinataire, message.as_string())
        server.quit()
        
        print('send')
        return True
    except Exception as e:
        print(f'error : {e}')
        return False


send_Email(
    destinataire='nzomutchawilfrid@gmail.com',
    sujet='<p color ="green">texte ne fonctionne pas</p>',
    corps_message='<p color ="green">texte ne fonctionne pas</p>'
)
