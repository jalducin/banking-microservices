# notifier-service/app/utils.py

def send_email(to_email: str, subject: str, message: str):
    print(f"Enviando email a {to_email} con asunto '{subject}': {message}")
