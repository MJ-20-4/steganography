import cv2
import os

def create_mapping():
    d = {chr(i): i for i in range(255)}
    c = {i: chr(i) for i in range(255)}
    return d, c

def embed_message(img, msg, d):
    n, m, z = 0, 0, 0
    for char in msg:
        img[n, m, z] = d[char]
        n += 1
        m += 1
        z = (z + 1) % 3
    return img

def extract_message(img, msg_length, c):
    message = ""
    n, m, z = 0, 0, 0
    for _ in range(msg_length):
        message += c[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3
    return message

def main():
    img_path = "E:\\stegano\\mypic.jpg"
    img = cv2.imread(img_path)
    
    msg = input("Enter secret message: ")
    password = input("Enter a passcode: ")
    
    d, c = create_mapping()
    img = embed_message(img, msg, d)
    cv2.imwrite("encryptedImage.jpg", img)
    os.system("start encryptedImage.jpg")
    
    pas = input("Enter passcode for Decryption: ")
    if password == pas:
        decrypted_message = extract_message(img, len(msg), c)
        print("Decryption message:", decrypted_message)
    else:
        print("YOU ARE NOT authorized")

if __name__ == "__main__":
    main()
