import os
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials
from googleapiclient.http import MediaFileUpload
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow
import httplib2

CLIENT_SECRETS_FILE = os.path.abspath('./credintial.json')

# This OAuth 2.0 access scope allows an application to upload files to the
# authenticated user's YouTube channel, but doesn't allow other types of access.
YOUTUBE_UPLOAD_SCOPE = "https://www.googleapis.com/auth/youtube.upload"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def get_authenticated_service():
    flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
                                   scope=YOUTUBE_UPLOAD_SCOPE,
                                   message="MISSING_CLIENT_SECRETS_MESSAGE")

    storage = Storage(os.path.abspath("app.py-oauth2.json"))
    credentials = storage.get()

    if credentials is None or credentials.invalid:
        credentials = run_flow(flow, storage)

    return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                 http=credentials.authorize(httplib2.Http()))

def videoUpload(title,description,video_file,status,tags,authPath):
    # Authenticate the API client
    creds = Credentials.from_authorized_user_file(authPath, ['https://www.googleapis.com/auth/youtube.upload'])
    # Create the YouTube API client
    youtube = build('youtube', 'v3', credentials=creds)

    # Define the video metadata
    request_body = {
        'snippet': {
            'title': title,
            'description': description,
            'categoryId': '22',
            'tags': tags
        },
        'status': {
            'privacyStatus': status
        }
    }

    # Upload the video
    try:
        # Create a video insert request and execute it
        insert_request = youtube.videos().insert(
            part='snippet,status',
            body=request_body,
            media_body=MediaFileUpload(video_file)
        )
        response = insert_request.execute()
        # Print the response
        return "https://www.youtube.com/watch?v="+response["id"]

    except HttpError as error:
        print(f'An HTTP error {error.resp.status} occurred: {error.content}')
        return None

if __name__=="__main__":
    title=""
    description=""
    video_file=""
    status="private"
    get_authenticated_service()
    videoUpload(title,description,video_file,status)
