from setuptools import setup

package_name = 'village_li'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lxp',
    maintainer_email='382023823@qq.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "li4=village_li.li4:main",
            "li5=village_li.li5:main",
            "li6=village_li.li6:main",
        ],
    },
)
