import unittest
import queue
import os
import uuid


TEST_FILE_NAME = './%s.txt' % uuid.uuid4()

queue.SCANNED_DATA_FILENAME = TEST_FILE_NAME


class EmptyScannedNumbers(unittest.TestCase):
    def test(self):
        if os.path.exists(TEST_FILE_NAME):
            os.remove(TEST_FILE_NAME)

        buffer = queue.read_list()

        self.assertEqual(buffer, [])


class TwoItemsInList(unittest.TestCase):
    def test(self):
        output = open(TEST_FILE_NAME, 'wt')
        output.write('apple\n')
        output.write('ball\n')
        output.close()

        buffer = queue.read_list()

        self.assertEqual(buffer, ['apple', 'ball'])


class KeyExists(unittest.TestCase):
    def test(self):
        output = open(TEST_FILE_NAME, 'wt')
        output.write('apple\n')
        output.write('ball\n')
        output.close()

        buffer = queue.read_list()

        result = queue.key_exists('apple', buffer)

        self.assertEqual(result, True)


class KeyDoesntExists(unittest.TestCase):
    def test(self):
        output = open(TEST_FILE_NAME, 'wt')
        output.write('apple\n')
        output.write('ball\n')
        output.close()

        buffer = queue.read_list()

        result = queue.key_exists('sua', buffer)

        self.assertEqual(result, False)


class AddKey(unittest.TestCase):
    def test(self):
        output = open(TEST_FILE_NAME, 'wt')
        output.write('apple\n')
        output.write('ball\n')
        output.close()

        buffer = queue.read_list()

        result = queue.key_exists('frog', buffer)

        self.assertEqual(result, False)

        queue.add_key('frog')

        new_buffer = queue.read_list()
        new_assert = queue.key_exists('frog', new_buffer)
        self.assertEqual(new_assert, True)


class AddKeyToBlankFile(unittest.TestCase):
    def test(self):
        if os.path.exists(TEST_FILE_NAME):
            os.remove(TEST_FILE_NAME)

        buffer = queue.read_list()

        result = queue.key_exists('frog', buffer)

        self.assertEqual(result, False)

        queue.add_key('frog')

        new_buffer = queue.read_list()
        new_assert = queue.key_exists('frog', new_buffer)
        self.assertEqual(new_assert, True)


class CreateKey(unittest.TestCase):
    def test(self):
        row = '0c:f3:ee:00:f6:33,8deefbb9f7384297804096668bb44281,5000,3221,-63,-78'
        key = queue.create_key(row)

        self.assertEqual(key, '8deefbb9f7384297804096668bb44281_5000_3221')


class QueueItem(unittest.TestCase):
    def test(self):
        row = '0c:f3:ee:00:f6:33,8deefbb9f7384297804096668bb44281,5000,3221,-63,-78'
        queue.queue_beacon(row)

        #
        # check the key exists
        #
        buffer = queue.read_list()
        key = '8deefbb9f7384297804096668bb44281_5000_3221'
        new_assert = queue.key_exists(key, buffer)
        self.assertEqual(new_assert, True)


class QueueMultipleItems(unittest.TestCase):
    def test(self):
        if os.path.exists(TEST_FILE_NAME):
            os.remove(TEST_FILE_NAME)

        row = '0c:f3:ee:00:f6:33,8deefbb9f7384297804096668bb44281,5000,3221,-63,-78'
        queue.queue_beacon(row)

        #
        # check the key exists
        #
        buffer = queue.read_list()
        key = '8deefbb9f7384297804096668bb44281_5000_3221'
        new_assert = queue.key_exists(key, buffer)
        self.assertEqual(new_assert, True)

        row2 = '0c:f3:ee:00:f6:33,8deefbb9f7384297804096668bb44281,5001,3221,-63,-78'
        queue.queue_beacon(row2)

        #
        # check the key exists
        #
        buffer2 = queue.read_list()
        key2 = '8deefbb9f7384297804096668bb44281_5001_3221'
        new_assert2 = queue.key_exists(key2, buffer2)
        self.assertEqual(new_assert2, True)

        new_assert3 = queue.key_exists(key, buffer2)
        self.assertEqual(new_assert3, True)


class RemoveItem(unittest.TestCase):
    def test(self):
        row = '0c:f3:ee:00:f6:33,8deefbb9f7384297804096668bb44281,5000,3221,-63,-78'
        queue.queue_beacon(row)

        #
        # check the key exists
        #
        buffer = queue.read_list()
        key = '8deefbb9f7384297804096668bb44281_5000_3221'
        new_assert = queue.key_exists(key, buffer)
        self.assertEqual(new_assert, True)

        #
        # Act
        #
        queue.remove_key(key)

        #
        # Assert
        #
        buffer2 = queue.read_list()
        new_assert2 = queue.key_exists(key, buffer2)
        self.assertEqual(new_assert2, False)


class TestJunk(unittest.TestCase):
    def test(self):
        queue.SCANNED_DATA_FILENAME = './junk.test'
		
		#
        # check the key exists
        #
        buffer = queue.read_list()
        key = '8deefbb9f7384297804096668bb44281_5000_3221'
        new_assert = queue.key_exists(key, buffer)
        self.assertEqual(new_assert, True)
        for item in buffer:
            print(item)

        queue.SCANNED_DATA_FILENAME = TEST_FILE_NAME


if __name__ == '__main__':
    unittest.main()
