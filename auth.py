import os
import json
import requests
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# Define the OAuth 2.0 scopes
SCOPES = ["https://www.googleapis.com/auth/fitness.activity.read"]

# Path to client_secret.json (downloaded from Google Cloud Console)
CLIENT_SECRET_FILE = "client_secret.json"

def authenticate_google_fit():
    creds = None
    token_path = "token.json"

    # Load existing tokens
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path)

    # If no valid credentials, authenticate again
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRET_FILE, 
                SCOPES
            )
            creds = flow.run_local_server(port=8000,redirect_uri_trusted="http://127.0.0.1:8000/")

        # Save the credentials
        with open(token_path, "w") as token_file:
            token_file.write(creds.to_json())

    return creds

if __name__ == "__main__":
    authenticate_google_fit()
    print("Authentication successful! Token saved in token.json.")
import json
import os
from google.oauth2.credentials import Credentials

def get_access_token():
    token_path = os.getenv("TOKEN_FILE")
    with open(token_path, "r") as file:
        data = json.load(file)
        return data["access_token"]
