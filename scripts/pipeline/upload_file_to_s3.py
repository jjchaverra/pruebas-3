import boto3
import sys

def main():
    
    print ("hola")
    print (sys.argv)
    bucket_name=sys.argv[1]
    aws_key=sys.argv[2]
    aws_access_key=sys.argv[3]
    aws_access_secret=sys.argv[4]
    local_path=sys.argv[5]

    print (bucket_name)
    print (aws_key)
    print (aws_access_key)
    print (aws_access_secret)
    print (local_path)

    session = boto3.Session(
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_access_secret,
    )
    client = session.client('s3')

    response = client.upload_file(
        local_path,
        bucket_name,
        
    )
    print ('Done uploading')


main()
