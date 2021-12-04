import pytest

{% if cookiecutter.async != 'true' -%}
@pytest.fixture(scope='session', autouse=True)
def client():
    from server import application
    return application.test_client()
{%- else %}
@pytest.fixture()
async def client(aiohttp_client):
    import importlib
    import server
    importlib.reload(server)
    return await aiohttp_client(server.app.app)
{%- endif %}
