# Image Labeler App

Simple web app for labeling images stored in S3. View images, label as YES/NO, add comments, and export results as CSV.

## Files

```
binary-image-labeling/
├── index.html              # Main web application
├── config.js               # AWS configuration (your settings)
├── convert_tiff_to_jpg.py  # Script to convert TIFF images to JPG
├── pyproject.toml          # Python dependencies
└── README.md               # This file
```

## Quick Setup

### 1. Configure AWS

Edit `config.js` with your values:

```javascript
const CONFIG = {
    AWS_REGION: 'eu-west-1',
    SOURCE_BUCKET: 'your-bucket',
    SOURCE_PREFIX: 'path/to/images/',
    OUTPUT_BUCKET: 'your-bucket', 
    OUTPUT_PREFIX: 'path/to/results/',
    IDENTITY_POOL_ID: 'eu-west-1:your-cognito-pool-id'
};
```

### 2. Set Up S3 Permissions

**Create Cognito Identity Pool:**
1. AWS Cognito Console → Create identity pool
2. Enable "unauthenticated identities"
3. Copy the Identity Pool ID to config.js

**Add IAM Policy to the unauthenticated role:**
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:GetObject", "s3:ListBucket"],
            "Resource": [
                "arn:aws:s3:::your-bucket",
                "arn:aws:s3:::your-bucket/*"
            ]
        },
        {
            "Effect": "Allow", 
            "Action": ["s3:PutObject"],
            "Resource": ["arn:aws:s3:::your-bucket/*"]
        }
    ]
}
```

**Configure S3 CORS:**
```json
[{
    "AllowedHeaders": ["*"],
    "AllowedMethods": ["GET", "PUT", "POST", "HEAD"],
    "AllowedOrigins": ["*"],
    "ExposeHeaders": ["ETag"]
}]
```

### 3. Convert TIFF Images (if needed)

```bash
pip install -r requirements.txt
python convert_tiff_to_jpg.py [aws-profile]
```

### 4. Deploy to AWS Amplify

1. AWS Amplify Console → New app → Host web app
2. Deploy without Git or connect repository
3. Upload `index.html` and `config.js`

## Usage

1. Open the deployed app URL
2. Images load automatically from S3
3. Click YES/NO to label each image
4. Add optional comments
5. Navigate with Previous/Next buttons
6. Click "Save Labels to S3" when done

## Output

CSV file saved to S3 with format:
```csv
image_id,labeled_positive,comment
"path/image1.jpg",true,"Good example"
"path/image2.jpg",false,"Not relevant"
```

## Troubleshooting

- **No images found**: Check bucket name, prefix, and file extensions
- **Access denied**: Verify Cognito permissions and S3 CORS
- **TIFF issues**: Use the conversion script or check browser console

## Supported Formats

- JPG, JPEG, PNG, GIF, WebP (native browser support)
- TIFF (with fallback to download link)