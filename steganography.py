from PIL import Image
import numpy as np
import os

def text_to_binary(text):
    binary = ''.join(format(ord(char), '08b') for char in text)
    return binary + '00000000' 

def binary_to_text(binary):
    binary = binary.split('00000000')[0]
    text = ''
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        text += chr(int(byte, 2))
    return text

def validate_image_path(path):
    if not os.path.exists(path):
        raise ValueError(f"Path does not exist: {path}")
    try:
        with Image.open(path) as img:
            img.verify()
    except Exception as e:
        raise ValueError(f"Invalid image file: {path}")

def validate_output_path(path):

    directory = os.path.dirname(path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
    if not path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.webp')):
        path += '.png'  
    return path

def hide_text(image_path, text, output_path):
    validate_image_path(image_path)
    output_path = validate_output_path(output_path)
    
    img = Image.open(image_path)
    img_array = np.array(img)
    
    binary_text = text_to_binary(text)
    
    if len(binary_text) > img_array.size:
        raise ValueError("Text is too long to hide in this image")
    
    flat_img = img_array.flatten()
    
    for i in range(len(binary_text)):
        flat_img[i] = (flat_img[i] & 254) | int(binary_text[i])
    
    img_array = flat_img.reshape(img_array.shape)
    
    result_img = Image.fromarray(img_array)
    result_img.save(output_path)
    print(f"Text hidden successfully in {output_path}")

def extract_text(image_path):

    validate_image_path(image_path)
    
    img = Image.open(image_path)
    img_array = np.array(img)
    
    flat_img = img_array.flatten()
    
    binary_text = ''
    for i in range(len(flat_img)):
        binary_text += str(flat_img[i] & 1)
        if binary_text[-8:] == '00000000':  
            break
    
    text = binary_to_text(binary_text)
    return text

def main():
    while True:
        print("\nSteganography Tool")
        print("1. Hide text in image")
        print("2. Extract text from image")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            print("\n=== Hide Text in Image ===")
            image_path = input("Enter the path of the input image: ")
            text = input("Enter the text to hide: ")
            output_path = input("Enter the path for the output image (including filename): ")
            try:
                hide_text(image_path, text, output_path)
            except Exception as e:
                print(f"Error: {e}")
                
        elif choice == '2':
            print("\n=== Extract Text from Image ===")
            image_path = input("Enter the path of the image containing hidden text: ")
            try:
                hidden_text = extract_text(image_path)
                print(f"\nHidden text: {hidden_text}")
            except Exception as e:
                print(f"Error: {e}")
                
        elif choice == '3':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 