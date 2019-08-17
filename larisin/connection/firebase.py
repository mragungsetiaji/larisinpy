import firebase_admin
import os.path

from firebase_admin import credentials
from firebase_admin import _utils
from firebase_admin.db import reference, Reference, _DatabaseService

_DB_ATTRIBUTE = '_database'

class FirebaseUtils(object):

    def __init__(self, CREDENTIALS_PATH=None, DB_URL=None):

        self.FIREBASE_CREDENTIALS_PATH = CREDENTIALS_PATH
        self.FIREBASE_DATABASE_URL = DB_URL

    def connect(self):
        """Initializes and returns a new App instance.

        Returns:
            app firebase instance connection.
        """
        # Check credentials service account is exist
        if not os.path.exists(self.FIREBASE_CREDENTIALS_PATH):
            return ValueError("FIREBASE_CREDENTIALS_PATH is not found.")

        # Fetch the service account key JSON file contents
        cred = credentials.Certificate(self.FIREBASE_CREDENTIALS_PATH)
        
        try:
            # Initialize the app with a service account, 
            # granting admin privileges
            app = firebase_admin.initialize_app(
                cred, {'databaseURL': self.FIREBASE_DATABASE_URL})

            print("Connected to Firebase DB : {}".format(
                        self.FIREBASE_DATABASE_URL))
            
            return app

        except:
            return ValueError('Ups. Maybe you are already connected to :' 
                              '{}'.format(self.FIREBASE_DATABASE_URL))

    def delete_connect(self, app):
        """Delete firebase connection

        Args:
            app : App instance
        Returns:
            Deleted connection
        """
        return firebase_admin.delete_app(app)

    def reference(self, path='/', app=None, url=None):
        
        service = _utils.get_app_service(app, _DB_ATTRIBUTE, _DatabaseService)
        client = service.get_client(url)
        return Reference(client=client, path=path)

    def get(self):
        return Reference().get(etag=False, shallow=False)

    def set(self, value):
        return Reference().set(value)

    def update(self, value):
        return Reference().update(value)

    