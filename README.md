# AWS Polly Text-to-Speech CI/CD Pipeline

A GitHub-based CI/CD pipeline that uses Amazon Polly and S3 to convert text content into audio.

## Setup

### AWS Credentials

Add these secrets to your GitHub repository (Settings → Secrets and variables → Actions):
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_REGION`
- `S3_BUCKET_BETA`
- `S3_BUCKET_PROD`

### S3 Buckets

Create two S3 buckets in AWS:
- `polly-project-beta`
- `polly-project-prod`

## How to Modify the Text

Edit `speech.txt` with your desired content.

## How to Trigger the Workflows

- **Pull request to main** → uploads to `polly-project-beta/polly-audio/beta.mp3`
- **Merge to main** → uploads to `polly-project-prod/polly-audio/prod.mp3`

## How to Verify the Uploaded Files

1. Go to S3 in the AWS Console
2. Navigate to your bucket
3. Open `polly-audio/` folder
4. Download and play the MP3 file