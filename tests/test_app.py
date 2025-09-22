import pytest
from app import app, entries


@pytest.fixture()
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        with c.session_transaction() as sess:
            sess["logged_in"] = True
        yield c


def test_add_entry(client):
    resp = client.post("/add_entry", data={"content": "Test Entry Content"})
    assert resp.status_code == 302
    assert resp.headers["Location"] == "/"
    assert len(entries) >= 1
    e = entries[-1]
    assert e.content == "Test Entry Content"


def test_add_entry_with_happiness(client):
    resp = client.post(
        "/add_entry",
        data={
            "content": "Test Entry Content",
            "happiness": "😃",
        },
    )
    assert resp.status_code == 302
    assert resp.headers["Location"] == "/"
    assert len(entries) >= 1
    e = entries[-1]
    assert e is not None
    assert e.content == "Test Entry Content"
    assert e.happiness == "😃"
