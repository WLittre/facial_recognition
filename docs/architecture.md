```mermaid
classDiagram
  class BoundingBox {
    +int x
    +int y
    +int width
    +int height
  }
  class Detection {
    +BoundingBox box
    +float confidence
  }
  class Embedding {
    +ndarray vector
    +int dimension
  }
  class FaceDetector {
    <<Protocol>>
    +detect(image) List~Detection~
  }
  class FaceEmbedder {
    <<Protocol>>
    +embed(face_image) Embedding
  }
  class FaceMatcher {
    <<Protocol>>
    +is_match(e1, e2) bool
  }
  class FaceRepository {
    <<Protocol>>
    +save(name, embedding)
    +find_closest(embedding) str
  }
  class OpenCVDetector {
    +detect(image) List~Detection~
  }
  class FaceNetEmbedder {
    +embed(face_image) Embedding
  }
  class EuclideanMatcher {
    +is_match(e1, e2) bool
  }
  class FileRepository {
    +save(name, embedding)
    +find_closest(embedding) str
  }
  class RecognitionPipeline {
    -FaceDetector detector
    -FaceEmbedder embedder
    -FaceMatcher matcher
    -FaceRepository repository
    +run(image) str
  }
  FaceDetector <|.. OpenCVDetector
  FaceEmbedder <|.. FaceNetEmbedder
  FaceMatcher <|.. EuclideanMatcher
  FaceRepository <|.. FileRepository
  Detection --> BoundingBox
  RecognitionPipeline --> FaceDetector
  RecognitionPipeline --> FaceEmbedder
  RecognitionPipeline --> FaceMatcher
  RecognitionPipeline --> FaceRepository
  FaceEmbedder ..> Embedding
  ```