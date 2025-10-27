// ============================================
// AWS CONFIGURATION - EXAMPLE TEMPLATE
// ============================================
// Copy this file to config.js and update with your actual values

const CONFIG = {
    // AWS Region where your buckets are located
    AWS_REGION: 'eu-central-1',
    
    // Source bucket containing images to label
    SOURCE_BUCKET: 'my-images-bucket',
    
    // Optional prefix/folder in source bucket
    // Examples: 'images/', 'photos/2024/', or '' for root
    SOURCE_PREFIX: 'images/',
    
    // Output bucket where CSV files will be saved
    // Can be the same as SOURCE_BUCKET or different
    OUTPUT_BUCKET: 'my-output-bucket',
    
    // Prefix for saved CSV files in output bucket
    OUTPUT_PREFIX: 'labels/',
    
    // Cognito Identity Pool ID for authentication
    // Get this from AWS Cognito Console after creating an identity pool
    // Format: 'region:uuid' (e.g., 'eu-central-1:12345678-1234-1234-1234-123456789012')
    IDENTITY_POOL_ID: 'eu-central-1:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
};
