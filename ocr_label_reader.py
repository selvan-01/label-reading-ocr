"""
Project: Label Reading using OCR
Description: This program extracts text from an image using Tesseract OCR
             and saves the extracted text into a file.
"""

# Import required libraries
from PIL import Image
import pytesseract


# Configure Tesseract OCR path (Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text_from_image(image_path):
    """
    Extract text from an image using Tesseract OCR.

    Parameters:
        image_path (str): Path to the input image

    Returns:
        str: Extracted text from the image
    """
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text
    except Exception as error:
        print("Error processing image:", error)
        return ""


def save_text_to_file(text, output_file="output/results.txt"):
    """
    Save extracted text into a file.

    Parameters:
        text (str): Text to be written
        output_file (str): Output file path
    """
    try:
        with open(output_file, "a") as file:
            file.write(text + "\n")

        print("✅ Text successfully written to file.")
    except Exception as error:
        print("Error writing to file:", error)


def main():
    """
    Main function to run the OCR process.
    """

    # Input image path
    image_path = "data/test_images/test1.jpg"

    # Extract text
    extracted_text = extract_text_from_image(image_path)

    # Print extracted text
    print("\n📄 Extracted Text:\n")
    print(extracted_text)

    # Save text to file
    save_text_to_file(extracted_text)


# Run the program
if __name__ == "__main__":
    main()