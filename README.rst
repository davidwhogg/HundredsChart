Hundreds Chart
==============

Hogg's musings on the elementary-school teaching tool.

License
-------

Copyright 2011, 2012 David W. Hogg (NYU).
**All rights reserved.**

Usage
-----

You need to have `python` and `pdflatex`.
Once these are installed, `git clone` the repo, `cd` into it and then::
    make
    open hundreds_chart.pdf

Notes
-----

Migrated from `cvs`.
First I added this line to the `CVSROOT/modules` file::

    teaching    book/teaching

Then I converted to git, preserving history using::

    cd ~
    git cvsimport -v -d howdy:/home/users/dwh2/cvsroot/ -C teaching teaching

Then I removed some files, made some changes, commited.
Then I merged with the github repo via::

    cd ~
    cd teaching
    git pull git@github.com:davidwhogg/HundredsChart.git
    git push git@github.com:davidwhogg/HundredsChart.git

Then I moved away all working copies (to `tmp`) and set myself up with::

    cd ~
    git clone git@github.com:davidwhogg/HundredsChart.git
