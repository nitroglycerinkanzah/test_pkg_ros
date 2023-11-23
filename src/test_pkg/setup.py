from setuptools import setup
import os
from glob import glob

package_name = 'test_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kanzie',
    maintainer_email='how about nooo',
    description='TODO: Package description',
    license='FERN Autonomous',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [ 
		'node = test_pkg.node:main'
        ],
    },
)
