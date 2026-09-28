from face_recognition_app.detection.models import BoundingBox

def test_bounding_box():

    fakeBox1 = BoundingBox(x=-1,y=20,width=50,height=50)
    fakeBox2 = BoundingBox(x=20,y=-1,width=50,height=50)
    fakeBox3 = BoundingBox(x=20,y=20,width=-1,height=50)
    fakeBox4 = BoundingBox(x=20,y=20,width=50,height=-1)

    fakeBox5 = BoundingBox(x=-1,y=-1,width=-1,height=-1)

    Box = BoundingBox(x=20,y=20,width=50,height=50)

