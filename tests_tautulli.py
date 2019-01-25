from tautulli import Tautulli
import unittest


class TestGetHistory(unittest.TestCase):
    """
    Test get_history()
    """

    def test_get_history(self):
        tautulli = Tautulli()
        hist_test_1_exp = 'Blade Runner 2049'

        resp = tautulli.get_history(
            length=1, media_type='movie', user='nettles4349'
        )
        hist_test_1_act = resp['response']['data']['data'][0]['full_title']

        self.assertEqual(hist_test_1_act, hist_test_1_exp)


if __name__ == '__main__':
    unittest.main()
