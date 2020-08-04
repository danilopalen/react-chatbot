from ibm_watson import AssistantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json

class Assistant_V1:
    
    APIKEY = "vZV1hfwjrjTXP9t4DFMCuJIJlR8tEZNY_LHdvI_NvgCY"
    ENDPOINT = "https://api.au-syd.assistant.watson.cloud.ibm.com/"    
    VERSION = "2020-04-01"
    WORKSPACE_ID = "afbb2b4c-eac7-4dde-a339-75f13c60c12c"

    def __init__(self):
        self._authenticate()

    def _authenticate(self):
        self.authenticator = IAMAuthenticator(self.APIKEY)
        self.assistant = AssistantV1(
                        version=self.VERSION,
                        authenticator=self.authenticator
                    )
        self.assistant.set_service_url(self.ENDPOINT)
        self.assistant.set_default_headers({'x-watson-learning-opt-out': "true"})

    def list_examples(self, intent):
        return self.assistant.list_examples(self.WORKSPACE_ID, intent).get_result()
    
    def message(self, msg=None, context=None):
        return self.assistant.message(
                    self.WORKSPACE_ID,
                    input=msg,
                    context=context
                ).get_result()
        
        
