from assistantV1 import Assistant_V1
import unittest
import json
import random

class TestAnythingElse(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.assistantv1 = Assistant_V1()
        cls.context = None

    def test_anything_else(self):
        msg = self._create_message("sleep")
        response = self.assistantv1.message(msg, self.context)
        self._save_context(response["context"])
        # print(json.dumps(response, indent=2))

        # MODIFY EXPECTED OUTPUTS HERE
        ex_output = [
                     {
                         "ex_text": ("I didn't understand. You can try rephrasing.",
                                     "Can you reword your statement? I'm not understanding.",
                                     "I didn't get your meaning."
                                    )
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

        
