from assistantV1 import Assistant_V1
# from assistantV2 import Assistant_V2
import unittest
import json
import random

class TestWelcomeQuote(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up fixtures when the class starts"""
        cls.assistantv1 = Assistant_V1()
        cls.context = None
        # cls.assistantv2 = Assistant_V2()
        # cls.assistantv2.create_session()

    def test_001_welcome(self):
        msg = self._create_message("")
        response = self.assistantv1.message(msg, self.context)
        self._save_context(response["context"])
        # print(json.dumps(response, indent=2))

        # MODIFY EXPECTED OUTPUTS HERE
        ex_output = [
                     {
                         "ex_text": ("How can I help you today?")
                     },
                     {
                         "ex_title": "",
                         "ex_label": ("Get a Claim", "Get a Quote"),
                         "ex_value": ("claim", "quote")
                     }
                    ]
        
        for idx, res in enumerate(response["output"]["generic"]):
            if res["response_type"] == "text":
                self._assert_text(res, ex_output[idx]["ex_text"])
            else: # "option"
                self._assert_option(res,
                                    ex_title=ex_output[idx]["ex_title"],
                                    ex_label=ex_output[idx]["ex_label"],
                                    ex_value=ex_output[idx]["ex_value"])

    def test_002_get_a_quote(self):
        utterance = self._get_utterance("quote")
        
        msg = self._create_message(utterance)
        response = self.assistantv1.message(msg, self.context)
        self._save_context(response["context"])
        # print(json.dumps(response, indent=2))

        # MODIFY EXPECTED OUTPUTS HERE
        ex_output = [
                     {
                         "ex_text": ("Before we begin, did you know you could trade in your old car or get Finance through us?")
                     },
                     {
                         "ex_title": "",
                         "ex_label": ("No thanks, I like my car.", "Trade-in", "Finance", "Back"),
                         "ex_value": ("car", "trade", "finance", "back")
                     }
                    ]
        
        for idx, res in enumerate(response["output"]["generic"]):
            if res["response_type"] == "text":
                self._assert_text(res, ex_output[idx]["ex_text"])
            else: # "option"
                self._assert_option(res,
                                    ex_title=ex_output[idx]["ex_title"],
                                    ex_label=ex_output[idx]["ex_label"],
                                    ex_value=ex_output[idx]["ex_value"])

    def test_003_no_I_like_my_car(self):
        utterance = self._get_utterance("car")
        
        msg = self._create_message(utterance)
        response = self.assistantv1.message(msg, self.context)
        self._save_context(response["context"])
        # print(json.dumps(response, indent=2))

        # MODIFY EXPECTED OUTPUTS HERE
        ex_output = [
                     {
                         "ex_text": ("""All good. Let's get started...

Do you have your rego on hand?""")
                     },
                     {
                         "ex_title": "",
                         "ex_label": ("Yes", "No", "Back"),
                         "ex_value": ("yes", "no", "back")
                     }
                    ]
        
        for idx, res in enumerate(response["output"]["generic"]):
            if res["response_type"] == "text":
                self._assert_text(res, ex_output[idx]["ex_text"])
            else: # "option"
                self._assert_option(res,
                                    ex_title=ex_output[idx]["ex_title"],
                                    ex_label=ex_output[idx]["ex_label"],
                                    ex_value=ex_output[idx]["ex_value"])

    def test_004_dont_know_rego(self):
        utterance = self._get_utterance("no")
        
        msg = self._create_message(utterance)
        response = self.assistantv1.message(msg, self.context)
        self._save_context(response["context"])
        # print(json.dumps(response, indent=2))

        # MODIFY EXPECTED OUTPUTS HERE
        ex_output = [
                     {
                         "ex_text": ("No worries, here are some essential quickfire questions.")
                     },
                     {
                         "ex_text": ("What is your car model?")
                     }
                    ]
        
        for idx, res in enumerate(response["output"]["generic"]):
            if res["response_type"] == "text":
                self._assert_text(res, ex_output[idx]["ex_text"])
            else: # "option"
                self._assert_option(res,
                                    ex_title=ex_output[idx]["ex_title"],
                                    ex_label=ex_output[idx]["ex_label"],
                                    ex_value=ex_output[idx]["ex_value"])

    def test_005_car_model(self):
        # utterance = self._get_utterance("no")
        
        msg = self._create_message("Honda")
        response = self.assistantv1.message(msg, self.context)
        self._save_context(response["context"])
        # print(json.dumps(response, indent=2))

        # MODIFY EXPECTED OUTPUTS HERE
        ex_output = [
                     {
                         "ex_text": ("Can I get the model year?")
                     }
                    ]
        
        for idx, res in enumerate(response["output"]["generic"]):
            if res["response_type"] == "text":
                self._assert_text(res, ex_output[idx]["ex_text"])
            else: # "option"
                self._assert_option(res,
                                    ex_title=ex_output[idx]["ex_title"],
                                    ex_label=ex_output[idx]["ex_label"],
                                    ex_value=ex_output[idx]["ex_value"])
                
    def test_006a_car_year_fail(self):
        # utterance = self._get_utterance("no")
        
        msg = self._create_message("Honda")
        response = self.assistantv1.message(msg, self.context)
        self._save_context(response["context"])
        # print(json.dumps(response, indent=2))

        # MODIFY EXPECTED OUTPUTS HERE
        ex_output = [
                     {
                         "ex_text": ("Please type a year, ex. 1988")
                     }
                    ]
        
        for idx, res in enumerate(response["output"]["generic"]):
            if res["response_type"] == "text":
                self._assert_text(res, ex_output[idx]["ex_text"])
            else: # "option"
                self._assert_option(res,
                                    ex_title=ex_output[idx]["ex_title"],
                                    ex_label=ex_output[idx]["ex_label"],
                                    ex_value=ex_output[idx]["ex_value"])

    def test_006b_car_year_success(self):
        # utterance = self._get_utterance("no")
        
        msg = self._create_message("1999")
        response = self.assistantv1.message(msg, self.context)
        self._save_context(response["context"])
        # print(json.dumps(response, indent=2))

        # MODIFY EXPECTED OUTPUTS HERE
        ex_output = [
                     {
                         "ex_text": ("Thanks for providing your car model and car year.")
                     },
                     {
                         "ex_title": "",
                         "ex_label": ("Continue", "Back"),
                         "ex_value": ("yes", "no")
                     }
                    ]
        
        for idx, res in enumerate(response["output"]["generic"]):
            if res["response_type"] == "text":
                self._assert_text(res, ex_output[idx]["ex_text"])
            else: # "option"
                self._assert_option(res,
                                    ex_title=ex_output[idx]["ex_title"],
                                    ex_label=ex_output[idx]["ex_label"],
                                    ex_value=ex_output[idx]["ex_value"])

    @classmethod
    def _save_context(cls, context):
        cls.context = context
        
    @staticmethod
    def _create_message(msg_text):
        message = {
            "text": msg_text
        }
        return message
    
    # Intended for assistant api v2
    # Using assistant api v1 to get user utterances in the intents
    # api v2 does not expose this capability
    '''
    @classmethod
    def tearDownClass(cls):
        cls.assistantv2.delete_session()
        
    @staticmethod
    def _create_message(msg_text):
        message = {
            "message_type:": "text",
            "text": msg_text,
            "options": {
                "return_context": True
            }
        }
        return message
    '''

    def _get_utterance(self, intent):
        return random.choice(self.assistantv1.list_examples(intent)["examples"])["text"]

    def _assert_text(self, text, ex_text):
        self.assertIn(text["text"], ex_text)

    def _assert_option(self, option, ex_title=None, ex_label=None, ex_value=None):
        self.assertEqual(option["title"], ex_title)

        for i, op in enumerate(option["options"]):
            with self.subTest(option_index = i):
                self.assertEqual(op["label"], ex_label[i])
                self.assertEqual(op["value"]["input"]["text"], ex_value[i])

    # def setUp(self):
    #    """Set up fixtures when a test method starts"""
    #    print("setUp")

    # def tearDown(self):
    #    """Clean up fixtures when a test method finishes"""
    #    print("tearDown")


