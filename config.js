// ============================================
// AWS CONFIGURATION
// ============================================
// Copy this file and update with your actual values
// DO NOT commit this file to Git if it contains real credentials

const CONFIG = {
    // AWS Region where your buckets are located
    AWS_REGION: 'eu-west-1',
    
    // Source bucket containing images to label
    SOURCE_BUCKET: 'patomorfologia-ai',
    
    // Optional prefix/folder in the source bucket (e.g., 'images/' or leave empty '')
    SOURCE_PREFIX: 'datasets/Non_melanoma_skin_cancer_segmentation_for_histopathology/Images_jpgs/',
    
    // Output bucket where CSV files will be saved
    OUTPUT_BUCKET: 'patomorfologia-ai',
    
    // Prefix for saved CSV files in the output bucket
    OUTPUT_PREFIX: 'datasets/Non_melanoma_skin_cancer_segmentation_for_histopathology/',
    
    // Cognito Identity Pool ID for authentication
    // Format: 'region:uuid' (e.g., 'eu-central-1:12345678-1234-1234-1234-123456789012')
    IDENTITY_POOL_ID: 'eu-west-1:8940b17a-73c2-400b-9b51-90b2d426080c'
};
