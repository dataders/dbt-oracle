"""
Copyright (c) 2022, Oracle and/or its affiliates.
Copyright (c) 2020, Vitor Avancini

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

     https://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
"""

"""The setup script."""
from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

requirements = [
        "dbt-core==0.21.1; python_version < '3.7'",
        "dbt-core==1.0.4; python_version >= '3.7'",
        "cx_Oracle==8.3.0",
        "dataclasses; python_version < '3.7'"
]

test_requirements = [
    "pytest-dbt-adapter==0.4.0; python_version < '3.7'",
    "pytest-dbt-adapter==0.6.0; python_version >= '3.7'"
]

project_urls = {
    'Documentation': ' https://dbt-oracle.readthedocs.io',
    'Source': 'https://github.com/oracle-samples/dbt-oracle'
}

VERSION='1.0.0'
setup(
    author="Oracle",
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    description="dbt (data build tool) adapter for the Oracle database",
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='Oracle dbt',
    name='dbt-oracle',
    packages=find_packages(),
    test_suite='tests',
    tests_require=test_requirements,
    project_urls=project_urls,
    version=VERSION,
    zip_safe=False,
    package_data={
        'dbt': [
            'include/oracle/dbt_project.yml',
            'include/oracle/profile_template.yml',
            'include/oracle/macros/*.sql',
            'include/oracle/macros/**/**/*.sql'
        ]
    }
)
