from setuptools import setup

setup(name='elastic-template-cloner',
      version='0.1',
      description='copy elastic templates across clusters',
      long_description='Really, the funniest around.',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6.3',
      ],
      keywords='elastic template clone copy migration',
      url='https://github.com/chrismolica/elastic-template-cloner',
      author='Chris Molica',
      license='MIT',
      packages=['elastic-template-cloner'],
      install_requires=[
  'argparse',
  'json',
  'urllib2',
  'requests'],
      include_package_data=True,
      zip_safe=False)