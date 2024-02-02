===============
Boxes.py builds
===============

Record of `boxes.py <https://www.festi.info/boxes.py/>`_ builds.


Install
-------

.. code-block:: text

    poetry env use python3.9
    poetry install


Use
---

Execute invoke tasks:

.. code-block:: text

    poetry shell
    invoke --list
    invoke task1 ... taskN

Execute a custom generator:

.. code-block:: text

    BOXES_GENERATOR_PATH=generators boxes BurnTestCustom --date=1 --id="my identifier"
