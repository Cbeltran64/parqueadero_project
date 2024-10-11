import logging

logger = logging.getLogger(__name__)

def log_tariff_change(user, action, tariff):
    logger.info(f"El usuario {user} ha {action} la tarifa {tariff.nombre_tarifa}.")

def log_convenio_change(user, action, convenio):
    logger.info(f"El usuario {user} ha {action} el convenio {convenio.nombre_convenio}.")
