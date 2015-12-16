import unittest
import keepalive
import datetime


class SetDate(unittest.TestCase):
    def test(self):
        keepalive.initialise()

        self.assertIsNotNone(keepalive.LAST_RUN)


class CheckDifference(unittest.TestCase):
    def test(self):
        keepalive.initialise()

        delta = datetime.timedelta(seconds=10)

        keepalive.LAST_RUN = datetime.datetime.now() - delta

        difference = keepalive.time_difference()

        self.assertEqual(difference, 10)


class CheckTriggerDoesNotTrigger(unittest.TestCase):
    def test(self):
        keepalive.initialise()

        delta = datetime.timedelta(seconds=59)

        keepalive.LAST_RUN = datetime.datetime.now() - delta

        result = keepalive.check_keepalive()

        self.assertEqual(result, None)


class CheckTrigger(unittest.TestCase):
    def test(self):
        keepalive.initialise()

        delta = datetime.timedelta(seconds=61)

        keepalive.LAST_RUN = datetime.datetime.now() - delta

        result = keepalive.check_keepalive()

        self.assertEqual(result, "%s" % keepalive.format_datetime(datetime.datetime.now()))


class CheckTriggerResets(unittest.TestCase):
    def test(self):
        keepalive.initialise()

        delta = datetime.timedelta(seconds=61)

        keepalive.LAST_RUN = datetime.datetime.now() - delta

        result = keepalive.check_keepalive()

        self.assertEqual(result, "%s" % keepalive.format_datetime(datetime.datetime.now()))

        result_2 = keepalive.check_keepalive()

        self.assertEqual(result_2, None)


if __name__ == '__main__':
    unittest.main()
