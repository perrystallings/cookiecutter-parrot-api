from parrot_api.core import get_settings, create_server, configure_default_log_attributes
import os


app_settings = get_settings(env_folder=os.getenv('SETTINGS_FOLDER', '/apps/settings'))
configure_default_log_attributes(attributes=dict(
    service_name=app_settings['service_name'],
    environment=app_settings['environment']
))
current_directory = os.path.abspath(__file__).replace('server.py', '')
{% if cookiecutter.async != 'true' -%}
app = create_server(
    spec_dir=os.path.join(current_directory, './schemas/'), debug=app_settings['environment'] not in {'qa', 'prod'}
)
{% else -%}
app = create_server(
    spec_dir=os.path.join(current_directory, './schemas/'), debug=app_settings['environment'] not in {'qa', 'prod'},
    sync=False
)
{%- endif %}

application = app.app
