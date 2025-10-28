#!/usr/bin/env python3
"""
Convert TIFF images in S3 to JPG format
"""

import boto3
from PIL import Image
import io
import os
import sys

from dotenv import load_dotenv

load_dotenv()

BUCKET_NAME = os.getenv('BUCKET_NAME')
SOURCE_PREFIX = os.getenv('SOURCE_PREFIX')
TARGET_PREFIX = os.getenv('TARGET_PREFIX')
AWS_REGION = os.getenv('AWS_REGION')

def convert_tiff_to_jpg(profile_name='kraftcode'):
    session = boto3.Session(profile_name=profile_name)
    s3 = session.client('s3', region_name=AWS_REGION)
    
    # List all TIFF files
    response = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix=SOURCE_PREFIX)
    
    if 'Contents' not in response:
        print("No files found in the specified prefix")
        return
    
    tiff_files = [obj['Key'] for obj in response['Contents'] 
                  if obj['Key'].lower().endswith(('.tif', '.tiff'))]
    
    print(f"Found {len(tiff_files)} TIFF files to convert")
    
    for i, tiff_key in enumerate(tiff_files, 1):
        try:
            print(f"Converting {i}/{len(tiff_files)}: {tiff_key}")
            
            # Download TIFF from S3
            response = s3.get_object(Bucket=BUCKET_NAME, Key=tiff_key)
            tiff_data = response['Body'].read()
            
            # Convert TIFF to JPG
            with Image.open(io.BytesIO(tiff_data)) as img:
                # Convert to RGB if necessary
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                
                # Save as JPG to memory
                jpg_buffer = io.BytesIO()
                img.save(jpg_buffer, format='JPEG', quality=95)
                jpg_buffer.seek(0)
                
                # Create new key with JPG extension
                filename = os.path.basename(tiff_key)
                jpg_filename = os.path.splitext(filename)[0] + '.jpg'
                jpg_key = TARGET_PREFIX + jpg_filename
                
                # Upload JPG to S3
                s3.put_object(
                    Bucket=BUCKET_NAME,
                    Key=jpg_key,
                    Body=jpg_buffer.getvalue(),
                    ContentType='image/jpeg'
                )
                
                print(f"  → Saved as: {jpg_key}")
                
        except Exception as e:
            print(f"  ✗ Error converting {tiff_key}: {e}")
    
    print("Conversion complete!")

if __name__ == "__main__":
    """
    Convert TIFF images in S3 to JPG format
    
    Usage: python convert_tiff_to_jpg.py [profile]
    Default profile is 'kraftcode'. If profile is not specified, uses default credentials.
    """
    profile = sys.argv[1] if len(sys.argv) > 1 else 'kraftcode'
    print(f"Using AWS profile: {profile}")
    convert_tiff_to_jpg(profile_name=profile)