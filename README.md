# facial_recognition
I'll try to relearn Python basics, by doing some "Machine learning"

## Overview
This project aims to implement a basic facial recognition system using Python.

## Features
- It should be able to detect and recognize faces throughtout the webcam
- It should be able to store and manage known faces.

## Principes
- Detection: An algorithm will scan the input and draw BoundingBoxes where faces are detected.
- Preprocessing: Faces detected are tilted, rotated, or captured under varying angles or lighting conditions constantly on a camera, we have to normalize to improve recognition accuracy.
- Embedding: Neural networks are used to convert faces into high-dimensional vectors, capturing unique features for recognition. 
- Matching: We calculate the euclidean distance between stored and detected face embeddings to determine if they match.
- Storage: The system will maintain a database or file system to store embeddings and associated metadata for known faces.