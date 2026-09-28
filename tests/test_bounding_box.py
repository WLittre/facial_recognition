import pytest
from face_recognition_app.detection.models import BoundingBox

def test_bounding_boxX():
    with pytest.raises(ValueError):
        fake_box1 = BoundingBox(x=-1,y=20,width=50,height=50)

def test_bounding_boxY():
    with pytest.raises(ValueError):
        fakeBox2 = BoundingBox(x=20,y=-1,width=50,height=50)

def test_bounding_box_width():
    with pytest.raises(ValueError):
        fakeBox3 = BoundingBox(x=20,y=20,width=-1,height=50)

def test_bounding_box_height():
    with pytest.raises(ValueError):
        fakeBox4 = BoundingBox(x=20,y=20,width=50,height=-1)

def test_bounding_box_null():
    with pytest.raises(ValueError):
        fakeBox5 = BoundingBox(x=0,y=0,width=0,height=50)
    
def test_bounding_box_negate():
    with pytest.raises(ValueError):
        fakeBox6 = BoundingBox(x=-1,y=-1,width=-1,height=-1)   
    
def test_bounding_box_valid():
    with pytest.raises(ValueError):
        Box = BoundingBox(x=20,y=20,width=50,height=50)       
def test_bounding_box_immutabe():
    with pytest.raises(FrozenInstanceError):
        Box.x = 10

    

