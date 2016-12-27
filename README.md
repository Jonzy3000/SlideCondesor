# SlideCondesor

Lecturer gives slides in a weird format, a new slide per new line. Which can be annoying to revise from. This simply condenses thes slides into whole and healthy slides, so no matching text is on the same two adjacent slides.

To use, simply have all your pdfs in the same dir as the two .py files, and run `python condenseAllSlidesInDir.py` This assumes that the slides are in a certain format, it seems to work for networking module so should work for every other module said lecturer prdouces slides for.

Relies on PyPDF2 - if you have pip installed simply `pip install PyPDF2` else can get it from [here](https://pypi.python.org/pypi/PyPDF2)