# Image Captioning App

This application provides a simple interface to generate captions for images using a pre-trained model from Hugging Face's Transformers library.

## Features
- **Image Captioning**: Automatically generate descriptive captions for uploaded images.
- **User-Friendly Interface**: Built using Gradio for an easy-to-use web interface.

## Model
- **Model Used**: `Salesforce/blip-image-captioning-base`
- **Framework**: Hugging Face Transformers

## Software Packages
- **Gradio**: Used to create the web interface.
- **Transformers**: Used for model inference.
- **Spaces**: Utilized for GPU acceleration during model execution.

## How to Use
- **Upload an Image**: Use the "Upload image" button to upload an image.
- **View Caption**: The app will automatically generate and display a caption for the image.
- **Caption Display**: The generated caption will appear in the textbox labeled "Caption".

## How to Install and Use the App Locally

### Prerequisites
- Python 3.8 or later
- `pip` package manager

#### Step 1: Clone the Repository
Clone the repository to your local machine using Git:

```bash
git clone <repository_url>
cd <repository_directory>
```

#### Step 2: Create a Virtual Environment

It is recommended to create a virtual environment to manage dependencies:

```bash
# Create a virtual environment
python -m venv venv

source venv/bin/activate
```

#### Step 3: Install Dependencies

Install the required Python packages using the requirements.txt file:

```bash
pip install -r requirements.txt
```

#### Step 4: Run the App

Once the dependencies are installed, you can start the app:

```bash
python app.py
```

The demo will open in a browser at `http://localhost:7860` if running from a file. If you are running within a notebook, the demo will appear embedded within the notebook.