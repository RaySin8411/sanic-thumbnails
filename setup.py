from distutils.core import setup

setup(
    name='Sanic-thumbnails',
    version='0.1',
    url='',
    license='MIT',
    author='raysin',
    author_email='ray0101.sin@gmail.com',
    description='A simple extension to create a thumbs for the Sanic',
    py_modules=['Sanic_thumbnails'],
    # packages=['Sanic_thumbnails'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Sanic',
        'Pillow',
    ],
)