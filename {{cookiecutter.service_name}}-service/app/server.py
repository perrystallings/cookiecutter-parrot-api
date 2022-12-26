from parrot_api.core import create_server
from startup import *
import os

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
