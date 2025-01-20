# 얼굴 비교 샘플 코드

import boto3

def compare_faces(sourceFile, targetFile):

    client = boto3.client('rekognition')

    imageSource = open(sourceFile, 'rb')
    imageTarget = open(targetFile, 'rb')

    response = client.compare_faces(SimilarityThreshold=0,
                                    SourceImage={'Bytes': imageSource.read()},
                                    TargetImage={'Bytes': imageTarget.read()})

    for faceMatch in response['FaceMatches']:
        result = '동일 인물일 확률은 {:.2f}%입니다'.format(faceMatch['Similarity'])

    imageSource.close()
    imageTarget.close()
    return result
