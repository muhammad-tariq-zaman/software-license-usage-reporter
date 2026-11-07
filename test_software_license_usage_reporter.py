import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import report

def row(s, owned, used):
    return {"software": s, "licences_owned": str(owned), "licences_used": str(used)}

class TestLicenceUsage(unittest.TestCase):
    def test_usage_pct(self):
        self.assertAlmostEqual(report([row("App", 10, 5)])[0][3], 0.5)
    def test_overused(self):
        self.assertEqual(report([row("App", 10, 12)])[0][4], "OVERUSED")
    def test_ok(self):
        self.assertEqual(report([row("App", 10, 8)])[0][4], "OK")
    def test_highest_first(self):
        r = report([row("A", 10, 2), row("B", 10, 9)])
        self.assertEqual(r[0][0], "B")
