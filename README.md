# Sanic-thumbnails


Install with ``pip``:

    pip install git+https://github.com/q8977452/sanic-thumbnails.git

Install:

    from sanic.ext.thumbnails import Thumbnail

    app = Sanic(__name__)

    thumb = Thumbnail(app)
    
Add ``UPLOAD_FOLDER`` in your settings:

    UPLOAD_FOLDER = '/home/www/media'
Use in Jinja2 template:

    {{ 'sc.jpg'|thumbnail('200x200') }}
    {{ object_img|thumbnail('200x200', crop='fit') }}
