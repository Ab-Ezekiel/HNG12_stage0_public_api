HNG12 Stage 0 Public API

This is a simple public API developed as part of the HNG Internship Stage 0 task. It returns basic information in JSON format, including:

    Your registered email (used in the HNG12 Slack workspace)
    The current datetime in ISO 8601 format
    The GitHub repository URL of this project

🛠 Tech Stack

    Programming Language: Python
    Framework: Flask
    Deployment: (Add your deployment platform, e.g., Render, Vercel, or Railway)

🚀 How to Run Locally
1️⃣ Clone the Repository

git clone https://github.com/Ab-Ezekiel/HNG12_stage0_public_api.git
cd HNG12_stage0_public_api

2️⃣ Set Up Virtual Environment

python3 -m venv venv  
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Run the API

python app.py

5️⃣ Test the API

Once the server is running, open your browser or use curl to test the endpoint:

curl http://127.0.0.1:5000

Expected JSON response:

{
  "email": "akpanabraham1000@gmail.com",
  "current_datetime": "2025-02-05T06:18:15.974429Z",
  "github_url": "https://github.com/Ab-Ezekiel/HNG12_stage0_public_api.git"
}

🌍 Public API URL

Your API is live at:
➡ YOUR_DEPLOYMENT_URL_HERE
(Replace with the actual deployed URL)
