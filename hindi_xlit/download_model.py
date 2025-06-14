"""
Script to download and set up the Hindi transliteration model
"""

import os
import zipfile
from pydload import dload
import torch

MODEL_DOWNLOAD_URL = 'https://github.com/AI4Bharat/IndianNLP-Transliteration/releases/download/xlit_v0.5.0/hindi.zip'
MODEL_VERSION = "v0.5"

def download_model():
    """Download and set up the Hindi transliteration model"""
    # Create models directory if it doesn't exist
    current_dir = os.path.dirname(os.path.abspath(__file__))
    models_path = os.path.join(current_dir, 'models')
    os.makedirs(models_path, exist_ok=True)
    
    # Check if model already exists
    model_path = os.path.join(models_path, 'hindi', 'hi_111_model.pth')
    if os.path.exists(model_path):
        print('Model already exists at:', model_path)
        return
    
    # Download model
    print('Downloading Hindi transliteration model...')
    downloaded_zip_path = os.path.join(models_path, 'hindi.zip')
    
    try:
        dload(url=MODEL_DOWNLOAD_URL, save_to_path=downloaded_zip_path, max_time=None)
        
        if not os.path.isfile(downloaded_zip_path):
            raise Exception(f'ERROR: Unable to download model from {MODEL_DOWNLOAD_URL}')
        
        # Extract the zip file
        with zipfile.ZipFile(downloaded_zip_path, 'r') as zip_ref:
            zip_ref.extractall(models_path)
        
        # Remove the zip file after extraction
        os.remove(downloaded_zip_path)
        
        print('Model downloaded and extracted successfully!')
        print(f'Model files are located at: {models_path}')
        
    except Exception as e:
        print(f'Error downloading model: {str(e)}')
        raise

if __name__ == '__main__':
    download_model() 