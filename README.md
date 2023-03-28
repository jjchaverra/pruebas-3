# s3-upload-github-action
Upload github action for sending files to s3


## Usage

This is a super straightforward action that uses the aws cli tool to copy a particular file to an s3 bucket. The file can come from your code directly or generated by an earlier part of your github actions flow. Check out the example below to get started.

Please note that each env var is requir878ed. It is recommended to put your AWS credentials in as repository secrets, as well as your bucket name.

```yaml
# inside .github/workflows/your-action.yml
name: Add File to Bucket
on: push

jobs:
  deploy:
    runs-on: ubuntu-latest
    
    steps:
   - uses: actions/checkout@master
   
   - name: Upload file to bucket
   uses: zdurham/s3-upload-github-action@master
   with:
     args: --acl public-read
   env:
    FILE: ./lambda.zip
    AWS_REGION: 'us-east-1'
    S3_BUCKET: ${{ secrets.AWS_S3_BUCKET }}
    S3_KEY: ${{ secrets.S3_KEY }}
    AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
    AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
```
