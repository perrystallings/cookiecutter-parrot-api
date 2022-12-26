import pytest

{% if cookiecutter.async != 'true' -%}
@pytest.fixture(scope='session', autouse=True)
def client():
    from server import application
    return application.test_client()
{%- else %}
@pytest.fixture()
@pytest.fixture(scope='session')
def event_loop():
    import asyncio
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture()
async def client(aiohttp_client):
    from server import application
    return await aiohttp_client(application)
{%- endif %}
