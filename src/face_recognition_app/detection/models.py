from dataclasses import dataclass


@dataclass(frozen=True)
class BoundingBox:
    x: int
    y: int
    width: int
    height: int

    def __post_init__(self) -> None:
        if self.x < 0 :
            raise ValueError(f"x ({self.x}) ne doit pas être négatif")
        if self.y < 0:
            raise ValueError(f"y ({self.y}) ne doit pas être négatif")
        if self.width <= 0:
            raise ValueError(f"la largeur ({self.width}) ne doit être négatif")
        if self.height <= 0:
            raise ValueError(f"la hauteur({self.height})  ne doit être négatif")