import setuptools

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name='ds_kit',
    version='1.0.0',
    author="Richard Raphael Banak",
    description="Data Quality System to help manage GCP automated process",
    url="https://github.com/Richardbnk/gcp_data_quality",
    packages=['ds_kit', 'ds_kit/tools', 'ds_kit/data_quality'],
    
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    install_requires=[required],
)
