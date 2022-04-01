from setuptools import setup


setup(
    name='fastapi project',
    version='0.0.2',
    author='Mutedop',
    author_email='',
    install_requires=[
        'fastapi',
        'uvicorn',
        'SQLAlchemy',
        'pytest',
        'requests',
        'python-dotenv',
    ],
    scripts=['app/main.py', 'scripts/scripts_db.py']
)
