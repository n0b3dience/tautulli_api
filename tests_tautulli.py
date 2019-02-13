from tautulli import Tautulli
import unittest


class TestTautulli(unittest.TestCase):
    """Test Tautulli() methods"""

    def test_get_history_0(self):

        tautulli = Tautulli()

        hist_test_exp = 'success'

        req = tautulli.get_history()
        hist_test_act = req['response']['result']

        self.assertEqual(hist_test_act, hist_test_exp)

    def test_get_history_1(self):
        tautulli = Tautulli()
        hist_test_exp = 'success'

        req = tautulli.get_history(
            user='nettles4349', out_type='json', length=10)
        hist_test_act = req['response']['result']

        self.assertEqual(hist_test_act, hist_test_exp)

    def test_get_server_id(self):
        tautulli = Tautulli()
        req = tautulli.get_server_id(hostname='192.168.1.7')
        self.assertIsNotNone(
            req,
            msg=":::ERROR::: 'Tautulli.get_server_id()' returned 'None'"
        )


if __name__ == '__main__':
    unittest.main()
