import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from fastapi.testclient import TestClient
from zencastr.main import app
#import zencastr

client = TestClient(app)
#client = TestClient(zencastr.main:app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == "OK"


def test_add_normal():
    response = client.post("/podcast", json={"title": "Foo Bar", "author": "The Foo Barters", "filename": "yakfile.mp3"})
    assert response.status_code == 200
    assert response.json()["podcast"]["title"] == "Foo Bar"
    assert response.json()["podcast"]["author"] == "The Foo Barters"
    assert response.json()["podcast"]["filename"] == "yakfile.mp3"


def test_add_invalid():
    response = client.post("/podcast", json={"author": "The Foo Barters", "filename": "yakfile.mp3"})
    assert response.json() == {'detail': [{'loc': ['body', 'title'],'msg': 'field required','type': 'value_error.missing'}]}

    response = client.post("/podcast", json={"title": "Foo Bar", "filename": "yakfile.mp3"})
    assert response.json() == {'detail': [{'loc': ['body', 'author'],'msg': 'field required','type': 'value_error.missing'}]}

    response = client.post("/podcast", json={"title": "Foo Bar", "author": "The Foo Barters"})
    assert response.json() == {'detail': [{'loc': ['body', 'filename'],'msg': 'field required','type': 'value_error.missing'}]}


def test_add_extra():
    response = client.post("/podcast", json={"title": "Foo Bar", "author": "The Foo Barters", "filename": "yakfile.mp3", "tags": ["boring", "super boring", "crap"]})
    assert response.status_code == 200
    assert response.json()["podcast"]["title"] == "Foo Bar"
    assert response.json()["podcast"]["author"] == "The Foo Barters"
    assert response.json()["podcast"]["filename"] == "yakfile.mp3"