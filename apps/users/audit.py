import logging

logger = logging.getLogger(__name__)

def log_login_attempt(username, status):
    message = f"Intento de inicio de sesión para el usuario {username} - {'Éxito' if status else 'Fallido'}"
    logger.info(message)

def log_permission_change(user, action):
    message = f"El usuario {user} ha {action} permisos."
    logger.info(message)
