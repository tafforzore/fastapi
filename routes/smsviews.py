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


def message_send(email):
    try:
        msg = MIMEMultipart()
        msg['Subject'] = 'Inscription'
        msg['From'] = 'nzomutchawilfrid@gmail.com'
        msg['To'] = email
        password = 'oqpgexwxokepuwpq'
        body = f'''
            <!DOCTYPE html>
            <html lang="fr">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Signalement d'une erreur</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        line-height: 1.6;
                        color: #333;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                        background-color: #f9f9f9;
                    }}
                    .container {{
                        max-width: 600px;
                        padding: 20px;
                        border: 1px solid #ccc;
                        border-radius: 5px;
                        background-color: #fff;
                        text-align: center;
                    }}
                    h2 {{
                        margin-top: 0;
                    }}
                    .error-details {{
                        margin-bottom: 20px;
                        text-align: left;
                    }}
                    .error-details p {{
                        margin: 0;
                        padding: 5px 0;
                    }}
                </style>
            </head>
            <body>

            <div class="container">
                <h2>Merci de vous etre Inscrit</h2>
                <div class="error-details">
                    <p>Bonjour,</p>
                    <p>Je tiens à vous informer qu'une erreur a été rencontrée sur [nom_de_la_page/le_service]. L'erreur se produit lorsque {type}.</p>
                    <p>Voici quelques détails supplémentaires sur l'erreur :</p>
                    <ul>
                    </ul>
                    <p>Merci de prendre en compte cette erreur et de la corriger dès que possible.</p>
                </div>
            </div>

            </body>
            </html>
            '''

        msg.attach(MIMEText(body, 'html'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(msg['From'], password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
    except Exception as e :
        print(f'Une erreur c\'est produite {e}')
