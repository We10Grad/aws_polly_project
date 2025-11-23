import json
import boto3
import datetime
import os

# Initialize AWS clients
s3_client = boto3.client('s3')
polly_client = boto3.client('polly')

def synthesize_speech(text, voice_id='Joanna', output_format='mp3'):
    """
    Synthesize speech from text using Amazon Polly.
    """
    response = polly_client.synthesize_speech(
        Text=text,
        VoiceId=voice_id,
        OutputFormat=output_format
    )
    if 'AudioStream' in response:
        return response['AudioStream'].read()
    else:
        raise Exception("Could not synthesize speech")

def lambda_handler(event, context):
    # Extract text from API request
    body = json.loads(event['body'])
    text = body['text']
    
    # Synthesize speech
    audio_bytes = synthesize_speech(text)
    
    # Create timestamp filename
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Get bucket and environment from environment variables
    bucket = os.environ['S3_BUCKET']
    environment = os.environ['ENVIRONMENT']
    
    # Upload to S3
    s3_key = f"polly-audio/{environment}/{timestamp}.mp3"
    s3_client.put_object(
        Bucket=bucket,
        Key=s3_key,
        Body=audio_bytes
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Success!',
            'file': s3_key
        })
    }