from parrot_api.core import get_settings, configure_default_log_attributes
import os


current_directory = os.getcwd()
app_settings = get_settings(env_folder=os.getenv('SETTINGS_FOLDER', '/apps/settings'))
configure_default_log_attributes(attributes=dict(
    service_name=app_settings['service_name'],
    environment=app_settings['environment']
))