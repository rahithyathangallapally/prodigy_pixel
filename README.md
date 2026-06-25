# PRODIGY_CS_02 - Pixel Manipulation for Image Encryption

## Overview

This project is developed as part of the Prodigy InfoTech Cyber Security Internship.

The application encrypts and decrypts images using pixel manipulation techniques. A secret key is applied to RGB pixel values during encryption and reversed during decryption to restore the original image.

## Features

* Image Encryption
* Image Decryption
* Pixel Value Manipulation
* First Pixel Comparison for Verification
* Original vs Encrypted vs Decrypted Image Visualization
* User-Friendly Menu Driven Program

## Technologies Used

* Python
* Pillow (PIL)
* Matplotlib

## Working Principle

### Encryption

Each RGB value is modified using:

Encrypted Pixel = (Original Pixel + Key) % 256

### Decryption

Original Pixel = (Encrypted Pixel - Key) % 256

## Project Structure

Pixel-Image-Encryption/

├── image_encryptor.py

├── sample.jpg

├── encrypted_image.png

├── decrypted_image.png

├── README.md

## Installation

pip install pillow matplotlib

## Run

python image_encryptor.py

## Output

* Generates encrypted_image.png
* Generates decrypted_image.png
* Displays Original, Encrypted, and Decrypted Images
* Shows Pixel Value Changes

## Learning Outcomes

* Image Processing Fundamentals
* Pixel-Level Manipulation
* Basic Cryptography Concepts
* Python File Handling
* Security-Oriented Programming

## Author

Rahithya
