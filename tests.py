import unittest

from os import listdir
from pathlib import Path
from baml_client.sync_client import b
from baml_client.types import Source
from baml_client.types import ContentType

tests_path = Path("./tests/")

class TestSourceParser(unittest.TestCase):
    """Tests the source parsing of the LLM. Perfers to give unknown over guessing, just to be safe.
    """
    
    def test_cnn_case(self):
        for file_name in listdir(tests_path / "cnn"):
            with open(tests_path / "cnn" / file_name, "r", encoding='utf-8', errors='ignore') as file:
                content = "\n".join(file.readlines())
                # Unknown is an okay response, just don't want the response to be wrong.
                assertion_bool = b.IdentifySource(content) == Source.CNN or b.IdentifySource(content) == Source.UNKNOWN
                self.assertTrue(assertion_bool)
                
    def test_bbc_case(self):
        for file_name in listdir(tests_path / "bbc"):
            with open(tests_path / "bbc" / file_name, "r", encoding='utf-8', errors='ignore') as file:
                content = "\n".join(file.readlines())
                assertion_bool = b.IdentifySource(content) == Source.BBC or b.IdentifySource(content) == Source.UNKNOWN
                self.assertTrue(assertion_bool)
                
    def test_reddit_case(self):
        for file_name in listdir(tests_path / "reddit"):
            with open(tests_path / "reddit" / file_name, "r", encoding='utf-8', errors='ignore') as file:
                content = "\n".join(file.readlines())
                assertion_bool = b.IdentifySource(content) == Source.REDDIT or b.IdentifySource(content) == Source.UNKNOWN
                self.assertTrue(assertion_bool)
                
    def test_unknown_case(self):
        for file_name in listdir(tests_path / "fox"):
            with open(tests_path / "fox" / file_name, "r", encoding='utf-8', errors='ignore') as file:
                content = "\n".join(file.readlines())
                self.assertEqual(b.IdentifySource(content), Source.UNKNOWN)
                
class TestFactAndOpinionParser(unittest.TestCase):
    """Tests the fact and opinion classification. No fallback case bc its a binary, all-inclusive output.
    """
    
    def test_fact_case(self):
        for file_name in listdir(tests_path / "fact"):
            with open(tests_path / "fact" / file_name, "r", encoding='utf-8', errors='ignore') as file:
                content = "\n".join(file.readlines())
                self.assertEqual(b.IdentifyContentType(content), ContentType.FACT)
                
    def test_opinion_case(self):
        for file_name in listdir(tests_path / "opinion"):
            with open(tests_path / "opinion" / file_name, "r", encoding='utf-8', errors='ignore') as file:
                content = "\n".join(file.readlines())
                self.assertEqual(b.IdentifyContentType(content), ContentType.OPINION)
                
if __name__ == "__main__":
    unittest.main()