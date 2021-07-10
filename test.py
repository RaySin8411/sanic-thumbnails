import os
import unittest

import sanic
from sanic_thumbnails import Thumbnail


class ThumbnailTestCase(unittest.TestCase):

    def setUp(self):
        app = sanic.Sanic(__name__)
        app.config['TESTING'] = True
        app.config['MEDIA_FOLDER'] = '/tmp/thumbnail'
        app.config['MEDIA_URL'] = '/uploads/'
        self.thumb = Thumbnail(app)

    async def test_create_missing_path(self):
        self.assertFalse(os.path.exists('/tmp/thumbnail/media/test/subtest/'))
        await self.thumb._get_path('/tmp/thumbnail/media/test/subtest/test.jpg')
        self.assertTrue(os.path.exists('/tmp/thumbnail/media/test/subtest/'))
        os.removedirs('/tmp/thumbnail/media/test/subtest/')

    async def test_create_thumb_name(self):
        name = await self.thumb._get_name('test', '.jpg', '200x200', 'fit', '100')
        self.assertEquals(name, 'test_200x200_fit_100.jpg')

        name = await self.thumb._get_name('test', '.jpg')
        self.assertEquals(name, 'test.jpg')

        name = await self.thumb._get_name('test', '.jpg', 100)
        self.assertEquals(name, 'test_100.jpg')

    async def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
