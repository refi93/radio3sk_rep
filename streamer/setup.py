import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    'py3k-bcrypt',
    'mock',
    ]

setup(name='streamer',
      version='0.0',
      description='streamer part of radio3.sk',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='project',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = project:main
      [console_scripts]
      initialize_project_db = project.scripts.initializedb:main
      """,
      )
