import unittest
from reactor import Reactor


class ReactorTest(unittest.TestCase):
    def test_run(self):
        Reactor().run()
