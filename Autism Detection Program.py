# Student Credentials
# Coded by Samad Karim niaisnov 2021, Email: samad.karim.alvi@gmail.com

# Please wait for the program after running it. If the image fails to load, then rerun the code, thanks!

# Implemented libraries
from PIL import Image
from fer import FER
from cv2 import imread

# Refining Image for AI model with the help of PIL library

image_refined = Image.open('Original Image.jpg')  # Photo by cottonbro from Pexels, taken under creative common license.

# printing the dimensions and format of the image to be analyzed.
print(image_refined.width, image_refined.height, image_refined.format)

print("******Please wait while the code runs completely!*******")

left = 400
top = 500
right = 3800
bottom = 4000
cropped = image_refined.crop((left, top, right, bottom))
# cropped.show()

# Converting image to grayscale
grayscale = cropped.convert('1')
grayscale.show()
cropped.save('Cropped image\\ cropped grayscale.jpeg')


# Detecting emotions of the human with FER module and printing the output
image_path = imread('Cropped image\\ cropped grayscale.jpeg')
detection = FER()
all_emotions = detection.detect_emotions(image_path)
all_emotion_list = list(all_emotions)
print(f'***This is the complete list of all emotions in the human:{all_emotion_list}')


image_path = imread('Cropped image\\ cropped grayscale.jpeg')
detection = FER()
top_emotion = detection.top_emotion(image_path)
top_emotion_list = list(top_emotion)
print(f'***This is the dominant emotion in the human: {top_emotion_list}')

# Converting FER output into list
converting_to_list = list(top_emotion)
mood, per = converting_to_list

# appending the detected mood and its percent dominance into two new lists.
emotion_detected = [mood]
per_detected = [per]

# Detecting and predicting whether the person is autistic or not, by defining a function.
# The function considers the odd behaviours to be autistic and the rest as normal!


def autism_detector(x):
    normal_emotions = ['happy', 'surprise']
    autistic_emotions = ['angry', 'neutral', 'sad', 'disgust']
    final_report = ''
    for a in x:
        if a in normal_emotions:
            final_report += 'The person under consideration is not autistic'
        else:
            if a in autistic_emotions:
                final_report += 'The person is autistic'
    return final_report


# Converting the percent ratio of the emotion into percentage.
def aut_percentage(x):
    per_ratio = 0
    for aa in x:
        per_ratio += float(aa)
    result = per_ratio * 100
    return result


# Printing the final results
print(f'{autism_detector(emotion_detected)}, with {aut_percentage(per_detected)}% of the odd emotion, which shows'
      f' a lack of interest.')
