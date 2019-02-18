from tautulli import Tautulli
import unittest


tautulli = Tautulli()


class TestTautulli(unittest.TestCase):
    """Test Tautulli() methods"""

    def test_get_history_0(self):
        """Check default get_history() fn"""
        req = tautulli.get_history()
        hist_test_act = req['response']['result']
        self.assertEqual(
            hist_test_act,
            'success',
            msg=":::ERROR::: 'test_get_history_1()' FAILED"
        )

    def test_get_history_1(self):
        """Check get_history() fn with kwargs"""
        req = tautulli.get_history(user='nettles4349', length=10)
        hist_test_act = req['response']['result']
        self.assertEqual(
            hist_test_act,
            'success',
            msg=":::ERROR::: 'test_get_history_1()' FAILED"
        )

    def test_get_server_id(self):
        """Check get_server_id() fn"""
        req = tautulli.get_server_id(hostname='192.168.1.7')
        self.assertIsNotNone(
            req,
            msg=":::ERROR::: 'Tautulli.get_server_id()' returned 'None'"
        )


if __name__ == '__main__':
    unittest.main()
