from setuptools import setup, find_packages

import rename_project


setup(
    name='rename_project',
    packages = ['rename_project'], 
    license='BSD',
    version=rename_project.__version__,
    description='RenameProject is a Django app to renaming the project of boilerplate',
    author='Jitender Singh',
    author_email='jitender0514@gmail.com',
    include_package_data=True,
    download_url='https://github.com/jitender0514/djnago-rename/archive/0.1.tar.gz',
    url='https://github.com/jitender0514/djnago-rename',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)