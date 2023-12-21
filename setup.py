from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='wtisdk',
    version='1.5.4',
    author='Melih Teke',
    author_email='me@mteke.com',
    description='WTI SDK for interacting with WTI devices',
    long_description=f"{long_description}\n\nFor more information, visit the [PyPI page](https://pypi.org/project/wtisdk/).\n\nYou can also connect with me on [LinkedIn](https://www.linkedin.com/in/melih-teke/).",
    long_description_content_type='text/markdown',
    url='https://github.com/melihteke/wtisdk',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    install_requires=[
        'requests',
        'urllib3',
    ],
)
