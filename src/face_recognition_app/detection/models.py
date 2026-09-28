from dataclasses import dataclass


@dataclass
class BoundingBox:
    def __init__(self, x:int, y:int, width:int, height:int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __post_init__(self) -> None:
        if self.x < 0 :
            raise ValueError("x ne doit être négatifs")
        elif self.y < 0:
            raise ValueError("y ne doit être négatifs")
        elif self.width < 0:
            raise ValueError("la profondeur ne doit être négatifs")
        elif self.height < 0:
            raise ValueError("la hauteur ne doit être négatifs")
        else :
            print("x="+self.x+"y="+self.y+"width="+self.width+"height="+self.height)