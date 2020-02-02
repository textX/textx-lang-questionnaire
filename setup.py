from setuptools import setup, find_packages

setup(name='textx-lang-questionnaire',
      version='0.1.0',
      packages=find_packages(),
      package_data={'': ['*.tx']},
      install_requires=["textx"],
      entry_points={
        'textx_languages': [
            'questionnaire = txquestionnaire:questionnaire',
          ]
      },
      )
