import boto3

neo_bucket = 'xxxxx'
neo_session = boto3.Session(aws_access_key_id='xxxx', aws_secret_access_key='xxxxx')
neo_s3 = neo_session.client('s3', endpoint_url='https://nos.jkt-1.neo.id')

s3_path = 'images'
destination_filename = 'test.jpg'
source_filename =


s3_fullname = f'{s3_path}/{destination_filename}'


neo_s3.upload_file(image_output, neo_bucket, s3_fullname, ExtraArgs={'ACL': 'public-read', 'ContentType':'image/png'})
url_neo = '{}/{}/{}'.format(neo_s3.meta.endpoint_url, neo_bucket, s3_fullname)