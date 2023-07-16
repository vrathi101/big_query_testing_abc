import setuptools
setuptools.setup(
  name = 'big_query_testing_abc',         # How you named your package
  packages = ['url_code'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'sample package',   # Give a short description about your library
  author = 'VEDANT RATHI',                   # Type in your name
  author_email = 'vedrathi10@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/vrathi101/big_query_testing_abc.git',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/vrathi101/big_query_testing_abc/archive/refs/tags/v_01.tar.gz',    # I explain this later on
  keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],   # Keywords that define your package best
  install_requires=[
    'pandas'],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.7',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
