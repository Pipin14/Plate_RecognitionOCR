import argparse
import torch
import torch.nn.functional as F

from torchvision import transforms
from PIL import Image
from model import CRNN
from split import LicensePlateSplitter


# Load the trained model
vocabulary = ['-','0','1','2','3','4','5','6','7','8','9',
              'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
idx2char = {k:v for k,v in enumerate(vocabulary, start=0)}
char2idx = {v:k for k,v in idx2char.items()}
num_chars = len(vocabulary)
rnn_hidden_size = 256
model = CRNN(num_chars=num_chars, rnn_hidden_size=rnn_hidden_size)
model.load_state_dict(torch.load('model.pt', map_location=torch.device('cpu')))

def decode(labels):
    tokens = F.softmax(labels, 2).argmax(2)
    tokens = tokens.numpy().T
    plates = []

    for token in tokens:
        chars = [idx2char[idx] for idx in token]
        plate = ''.join(chars)
        plates.append(plate)
    return plates

def remove_duplicates(text):
    if len(text) > 1:
        letters = [text[0]] + [letter for idx, letter in enumerate(text[1:], start=1) if text[idx] != text[idx-1]]
    elif len(text) == 1:
        letters = [text[0]]
    else:
        return ""
    return "".join(letters)

def correct_prediction(word):
    parts = word.split("-")
    parts = [remove_duplicates(part) for part in parts]
    corrected_word = "".join(parts)
    return corrected_word

# Function to perform text recognition on image
def perform_text_recognition(image_path, model):
    image = Image.open(image_path).convert('RGB')

    # Preprocess the image
    transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])
    image = transform(image)
    image = image.unsqueeze(0)

    # Perform inference
    with torch.no_grad():
        pred = model(image)
        pred = decode(pred)
        pred_plate_number = correct_prediction(pred[0])

    return pred_plate_number


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_path', type=str, help='Path to input image')
    args = parser.parse_args()

    # Perform text recognition on input image
    predicted_plate = perform_text_recognition(args.image_path, model)
    
    plate_splitter = LicensePlateSplitter()
    predicted_city = plate_splitter.split_license_plate_numbers(predicted_plate)
    
    # Print the plate number and city
    print('Plate Number : ', predicted_plate)
    print('City: ', predicted_city)
    