from app.core.config import config


class SecretsUtil:
    def get_secret(self, secret: str):
        try:
            with open(f"/run/secrets/{secret}", "r") as file:
                return file.read()
        except FileNotFoundError as e:
            config.logger.error(e)


secrets_util = SecretsUtil()