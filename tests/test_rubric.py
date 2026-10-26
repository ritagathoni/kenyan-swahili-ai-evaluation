import unittest
from src.rubric import validate_review,summarize,DIMENSIONS
class SwahiliTests(unittest.TestCase):
 def test_missing(self):self.assertEqual(len(validate_review({})),len(DIMENSIONS)+2)
 def test_valid(self):
  x={'id':'s','register':'informal','rationale':'ok','scores':{k:2 for k in DIMENSIONS}}
  self.assertEqual(summarize(x)['average'],2)
 def test_bool_invalid(self):
  x={'register':'formal','rationale':'ok','scores':{k:2 for k in DIMENSIONS}}
  x['scores']['meaning']=True
  self.assertTrue(validate_review(x))
if __name__=='__main__':unittest.main()
