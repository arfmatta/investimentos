from setuptools import setup, find_packages

setup(
   name='meu_investimento',
   version='0.1',
   packages=find_packages(),
   install_requires=[],
   author='Artur Mata',
   author_email='arturrogerio@gmail.com',
   description='Uma biblioteca para cálculos de investimentos. Exemplo do curso de MLEng da Fiap.',
   url='https://github.com/arfmatta/investimentos',
   classifiers=[
       'Programming Language :: Python :: 3',
       'License :: OSI Approved :: MIT License',
       'Operating System :: OS Independent',
   ],
   python_requires='>=3.6',
)
