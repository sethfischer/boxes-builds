===============
Boxes.py builds
===============

Record of `boxes.py <https://www.festi.info/boxes.py/>`_ builds.


Install
-------

.. code-block:: text

    poetry env use python3.12
    poetry install


Use
---

Execute invoke tasks:

.. code-block:: text

    poetry run invoke --list
    poetry run invoke task1 ... taskN

Execute a custom generator:

.. code-block:: text

    BOXES_GENERATOR_PATH=generators boxes BurnTestCustom --date=1 --id="my identifier"
