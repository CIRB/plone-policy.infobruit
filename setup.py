from setuptools import setup, find_packages

version = '1.0'

setup(name='policy.infobruit',
      version=version,
      description="A policy for the portal info bruit",
      long_description=open("README.rst").read() + "\n" +
                       open("CHANGES.txt").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['policy'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'plonetheme.ibgeinfobruit',
          'collective.ckeditor',
          'Solgema.fullcalendar',
          'collective.gallery',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
