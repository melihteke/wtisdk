from setuptools import setup, find_packages

setup(
    name='wtisdk',
    version='1.3',
    author='Melih Teke',
    author_email='me@mteke.com',
    description='WTI SDK for interacting with WTI devices',
    long_description='''
                        WTI SDK: Python SDK for interacting with WTI devices

                        The WTI SDK is a powerful Python library that enables developers to easily interact with WTI devices, providing a comprehensive set of functions for managing and controlling operational and configuration aspects.

                        Features:
                        - Retrieve the status information of WTI devices
                        - Add new entries to the device's operational data
                        - Modify existing operational data entries
                        - Update the device's configuration settings
                        - Get detailed information about the device's configuration
                        - Perform various other actions on both operational and configuration levels

                        With the WTI SDK, developers can streamline their integration with WTI devices, automate management tasks, and build robust applications that leverage the full capabilities of WTI devices.

                        For usage instructions and examples, please refer to the documentation available at: https://github.com/melihteke/wtisdk

                        For any questions or support, feel free to contact us at me@mteke.com.
                        ''',
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
    ],
    install_requires=[
        'requests',
        'urllib3',
    ],
)
