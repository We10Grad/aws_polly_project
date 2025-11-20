import boto3


polly = boto3.client('polly')

def read_text_file():
    """
    Read text content from speech.txt file.
    
    Returns:
    str: The content of the file.
    """
    with open('speech.txt', 'r') as f:
        content = f.read()
    return content
    
    
def synthesize_speech(text, voice_id='Joanna', output_format='mp3'):
    """
    Synthesize speech from text using Amazon Polly.

    Parameters:
    text (str): The text to be synthesized.
    voice_id (str): The voice ID to use for synthesis.
    output_format (str): The format of the output audio file.

    Returns:
    bytes: The synthesized speech audio in bytes.
    """
    response = polly.synthesize_speech(
        Text=text,
        VoiceId=voice_id,
        OutputFormat=output_format
    )

    if 'AudioStream' in response:
        return response['AudioStream'].read()
    else:
        raise Exception("Could not synthesize speech")
    

if __name__ == "__main__":
    # Read text file
    text = read_text_file()
    print("Text read successfully!")
    
    # Call synthesize_speech()
    audio_bytes = synthesize_speech(text)
    print("Speech synthesized successfully!")
    
    # Save to mp3 file
    with open('output.mp3', 'wb') as f:
        f.write(audio_bytes)
    
    # Print confirmation
    print("Audio saved to output.mp3")