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
        serveur_smtp = 'http://node160-eu.n0c.com'
        port_smtp = 465
        mot_de_passe = 'y*Dy8Q+.W8l888Ty8'

        server = smtplib.SMTP_SSL(serveur_smtp, port_smtp)
        server.login(expediteur, mot_de_passe)
        server.sendmail(expediteur, destinataire, message.as_string())
        server.quit()
        return True
    except Exception as e:
        return False




def envoyer_email(destinataire, sujet, corps_message, expediteur, mot_de_passe, serveur_smtp, port_smtp):
    # Générer un identifiant unique pour l'en-tête Message-ID
    message_id = str(uuid.uuid4())

    # Création de l'e-mail avec l'en-tête Message-ID
    message = MIMEMultipart()
    message['From'] = expediteur
    message['To'] = destinataire
    message['Subject'] = sujet
    message['Message-ID'] = f'<{message_id}@tandisgicaedef.cm>'  # Utilisez votre domaine correct ici

    # Ajout du corps du message
    message.attach(MIMEText(corps_message, 'plain'))

    # Connexion au serveur SMTP
    try:
        server = smtplib.SMTP_SSL(serveur_smtp, port_smtp)
        server.login(expediteur, mot_de_passe)
        server.sendmail(expediteur, destinataire, message.as_string())
        server.quit()
        print("E-mail envoyé avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'e-mail : {e}")

# Exemple d'utilisation de la fonction
envoyer_email(
    destinataire='nzomutchawilfrid@gmail.com',
    sujet='<p color ="green">texte ne fonctionne pas</p>',
    corps_message='<p color ="green">texte ne fonctionne pas</p>',
    expediteur='Tandisgicaedef@tandisgicaedef.cm',
    mot_de_passe='soXB)EnS$o}v',
    serveur_smtp='tandisgicaedef.cm',
    port_smtp=465
)
