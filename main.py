
import boto3
import os

ACCESS_KEY = os.environ.get('ACCESS_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')

s3 = boto3.client('s3')

def create_bucket(bucket_name):
    try:
        s3.create_bucket(Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint':'ap-northeast-1'})
        print("Bucket created successfully 🪣")
    except Exception as e:
        print("Bucket already exists with the same name 💀")
        return boto3.resource('s3').Bucket(bucket_name) # type: ignore
    return None
    

def list_buckets():
    try:
        response = s3.list_buckets()
        print("Printing bucket names 📃")
        for bucket in response['Buckets']:
            print(f'Bucket Name: {bucket["Name"]}')
    except Exception as e:
        print("You don't have any buckets 😒")
        print(e)
        return None
    return None


def select_bucket():
    try:
        bucket_name = input("Enter the bucket name to select 🪣: ")
        s3.head_bucket(Bucket=bucket_name) # type: ignore
        print("Bucket selected successfully 🪣")
    except Exception as e:
        print("Bucket doesn't exists with the same name 😒")
        print(e)
        return None
    return bucket_name


def upload_file(bucket_name, file_name):
    try:
        s3.upload_file(file_name, bucket_name, file_name)
        print("File uploaded successfully")
    except Exception as e:
        print("File already exists with the same name 😒")
        print(e)
        return None
    return None


if __name__=='__main__':
    bucket_name = input("Enter the bucket name to create 😅: ")
    bucket = create_bucket(bucket_name)
    list_buckets()
    bucket_name = select_bucket()
    file_name = input("Enter the file name: ")
    upload_file(bucket_name, file_name)
    print("File uploaded successfully 🗃️")
    print("Thank you for using our service 🙏")
