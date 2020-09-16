prerequisite - python version>3.5 should be installed.
1) Go to the location- ChatBot_Dependencies_Installer via cd command
2) Execute
pip install -r chatbotdep/requirements.txt --no-index --find-links chatbotdep
to install the libs and their dependencies
3) In a Python shell check the value of `nltk.data.path`
4) Choose one of the path that exists on your machine, and unzip the data folder(nltk_data) and copy files into the nltk_data directory.

ImportError: Missing optional dependency 'xlrd'. Install xlrd >= 1.0.0 for Excel support Use pip or conda to install xlrd.
