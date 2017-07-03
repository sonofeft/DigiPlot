
.. quickstart

QuickStart
==========

Verify tkinter Installed
------------------------

**In Theory** tkinter is included with all standard Python distributions.
(In practice, it might not be included.)
It's almost certainly there on a Windows machine, however,
on Linux you might have to try::

    sudo apt-get update
    sudo apt-get install python-tk
    sudo apt-get install python3-tk
    
In order to get tkinter/Tkinter for python 2 & 3.

You can test the installation from a terminal window with::

    >>> import Tkinter       # python2
    >>> Tkinter._test()      # python2
    
    >>> import tkinter       # python3
    >>> tkinter._test()      # python3

This should pop up a small test window.

Install DigiPlot
----------------

The easiest way to install DigiPlot is::

    pip install digiplot
    
        OR on Linux
    sudo pip install digiplot
        OR perhaps
    pip install --user digiplot

In case of error, see :ref:`internal_pip_error`

.. _internal_source_install:

Installation From Source
------------------------

Much less common, but if installing from source, then
the best way to install digiplot is still ``pip``.

After navigating to the directory holding DigiPlot source code, do the following::

    cd full/path/to/digiplot
    pip install -e .
    
        OR on Linux
    sudo pip install -e .
        OR perhaps
    pip install --user -e .
    
This will execute the local ``setup.py`` file and insure that the pip-specific commands in ``setup.py`` are run.

Running DigiPlot
----------------

After installing with ``pip``, there will be a launch command line program called **digiplot** or, on Windows, **digiplot.exe**. From a terminal or command prompt window simply type::

    digiplot

and DigiPlot will start. If not, then there may be an issue with your system path.
The path for the digiplot executable might be something like::

    /usr/local/bin/digiplot             (if installed with sudo pip install -e .)
         or 
    /home/<user>/.local/bin/digiplot    (if installed with pip install -e .)
         or 
    C:\Python27\Scripts\digiplot.exe    (on Windows)

Make sure your system path includes the above path to **digiplot**.


.. _internal_pip_error:

pip Error Messages
------------------

If you get an error message that ``pip`` is not found, see `<https://pip.pypa.io/en/latest/installing.html>`_ for full description of ``pip`` installation.

There might be issues with ``pip`` failing on Linux with a message like::


    InsecurePlatformWarning
            or    
    Cannot fetch index base URL https://pypi.python.org/simple/

Certain Python platforms (specifically, versions of Python earlier than 2.7.9) have the InsecurePlatformWarning. If you encounter this warning, it is strongly recommended you upgrade to a newer Python version, or that you use pyOpenSSL.    

Also ``pip`` may be mis-configured and point to the wrong PyPI repository.
You need to fix this global problem with ``pip`` just to make python usable on your system.


If you give up on upgrading python or fixing ``pip``, 
you might also try downloading the digiplot source package 
(and all dependency source packages)
from PyPI and installing from source as shown above at :ref:`internal_source_install`


