from distutils.core import setup

setup(
    name = 'jiebaWebApi',
    packages = ['jiebaWebApi'],
    version = '1.1',
    description = 'A Web Api for Jieba.',
    author = 'davidtnfsh',
    author_email = 'davidtnfsh@gmail.com',
    url = 'https://github.com/udicatnchu/jiebaWebApi',
    download_url = 'https://github.com/udicatnchu/jiebaWebApi/archive/v1.1.tar.gz',
    keywords = ['jieba', 'word segmentation'],
    classifiers = [],
    license='MIT',
    install_requires=[
        'jieba==0.38',
    ],
    zip_safe=True
)
