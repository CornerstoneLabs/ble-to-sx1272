import unittest
import keepalive
import datetime


class SetDate(unittest.TestCase):
    def test(self):
        keepalive.initialise()

        self.assertIsNotNone(keepalive.last_run)


class CheckDifference(unittest.TestCase):
    def test(self):
        keepalive.initialise()

        delta = datetime.timedelta(seconds=10)

        keepalive.last_run = datetime.datetime.now() - delta

        difference = keepalive.time_difference()

        self.assertEqual(difference, 10)


class CheckTriggerDoesNotTrigger(unittest.TestCase):
    def test(self):
        keepalive.initialise()

        delta = datetime.timedelta(seconds=59)

        keepalive.last_run = datetime.datetime.now() - delta

        result = keepalive.check_keepalive()

        self.assertEqual(result, False)


class CheckTrigger(unittest.TestCase):
    def test(self):
        keepalive.initialise()

        delta = datetime.timedelta(seconds=61)

        keepalive.last_run = datetime.datetime.now() - delta

        result = keepalive.check_keepalive()

        self.assertEqual(result, True)


class CheckTriggerResets(unittest.TestCase):
    def test(self):
        keepalive.initialise()

        delta = datetime.timedelta(seconds=61)

        keepalive.last_run = datetime.datetime.now() - delta

        result = keepalive.check_keepalive()

        self.assertEqual(result, True)

        result_2 = keepalive.check_keepalive()

        self.assertEqual(result_2, False)


if __name__ == '__main__':
    unittest.main()
