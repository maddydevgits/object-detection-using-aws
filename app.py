import cv2
import boto3
import gtts
import playsound

accessKey='' # ask admin to share access key
secretAccessKey='' # ask admin to share secret access
region='us-east-1'

camera=cv2.VideoCapture(0)
client=boto3.client('rekognition',aws_access_key_id=accessKey,aws_secret_access_key=secretAccessKey,region_name=region)
text=''
while True:
    res,frame=camera.read()
    if res:
        cv2.imshow('output',frame)
        cv2.imwrite('test.jpg',frame)
        cv2.waitKey(1000)
        imageSource=open('test.jpg','rb')
        response=client.detect_labels(Image={'Bytes':imageSource.read()})
        # print(response)
        for i in response['Labels']:
            # print(i['Name'])
            text+=''.join(i['Name']+' Found')
            text+='\n'

        break
# print(text)
t1 = gtts.gTTS(text,lang = 'en')
# save the audio file
t1.save("welcome.mp3")
playsound.playsound('welcome.mp3')
cv2.destroyAllWindows()
camera.release()
