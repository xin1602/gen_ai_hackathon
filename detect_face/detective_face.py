import boto3
from text_generation import generate

# 創建S3和Rekognition客户端
s3 = boto3.resource('s3')
rekognition = boto3.client('rekognition')

# 獲取S3圖片對象
bucket_name = 'face-images-v4dhe71e'
image_key = 'casino_people_face.jpg'
bucket = s3.Bucket(bucket_name)
image_object = bucket.Object(image_key)

# 將S3圖片數據傳遞給Rekognition
response = rekognition.detect_faces(Image={'Bytes': image_object.get()['Body'].read()}, Attributes=['ALL'])

person = response['FaceDetails'][0]
print('表情: ', person['Emotions'][0]['Type'])
print('年齡範圍: ', person['AgeRange'])
print('微笑: ', person['Smile']['Value'])

if  response['FaceDetails'][0]['Smile']['Value'] == False:
    print("警告:玩家看起來不太開心!\n正在啟動ai助理......")
    print("\nAI助理:")
    generate("將以下內容換句話說:  如果你覺得獎項都太小，很無趣的話，建議您到後方那排賠率較高的機台進行遊玩") 