import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = []

def main():
    """Shows basic usage of the Google Docs API and Google Drive API.
    Creates a new Google Doc and adds text.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        # Build the Docs and Drive services
        docs_service = build("docs", "v1", credentials=creds)
        drive_service = build("drive", "v3", credentials=creds)

        # 1. Create a new document
        title = "My New Document via Python"
        new_doc = docs_service.documents().create(body={"title": title}).execute()
        document_id = new_doc.get("documentId")
        print(f"Created document with ID: {document_id}")
        print(f"Document URL: docs.google.com{document_id}/edit")

        # 2. Add content to the document
        requests = [
            {
                "insertText": {
                    "location": {"index": 1},
                    "text": "Hello world! This document was created using the Google Docs API in Python."
                }
            }
        ]

        docs_service.documents().batchUpdate(
            documentId=document_id, body={"requests": requests}
        ).execute()
        print("Text inserted successfully.")

    except HttpError as err:
        print(f"An API error occurred: {err}")

if __name__ == "__main__":
    main()
