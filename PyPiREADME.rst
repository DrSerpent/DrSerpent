========================
Dr Serpent Documentation
========================

Description:
============

Dr Serpent 🐍  is an easy to use testing framework for Python focusing on Behaviour Driven Development and Test Driven Development processes.

Example:
========

.. code:: python

  # file
  def run():
      return 1 + 1

  # test_file
  def test_number():
    return Expect(run(2)).to_equal(2)

How to use:
===========

`Click Here <https://pypi.org/project/drserpent/>`_ to visit the PyPi URL.

View DrSerpent `documentation <https://github.com/DrSerpent/DrSerpent-Core/blob/master/DOCUMENTATION.md>`_

`Getting Started <https://github.com/DrSerpent/DrSerpent-Core/blob/master/DOCUMENTATION.md#getting-started>`_

`Compulsory Conventions <https://github.com/DrSerpent/DrSerpent-Core/blob/master/DOCUMENTATION.md#conventions>`_

Matchers:

- `to_equal <https://github.com/DrSerpent/DrSerpent-Core/blob/master/DOCUMENTATION.md#to_equal>`_
- `to_be_truthy <https://github.com/DrSerpent/DrSerpent-Core/blob/master/DOCUMENTATION.md#to_be_truthy>`_
- `to_be_falsey <https://github.com/DrSerpent/DrSerpent-Core/blob/master/DOCUMENTATION.md#to_be_falsey>`_
- `to_be_none <https://github.com/DrSerpent/DrSerpent-Core/blob/master/DOCUMENTATION.md#to_be_none>`_
- `to_be_greater_than <https://github.com/DrSerpent/DrSerpent-Core/blob/master/DOCUMENTATION.md#to_be_greater_than>`_
- `to_be_less_than <https://github.com/DrSerpent/DrSerpent-Core/blob/master/DOCUMENTATION.md#to_be_less_than>`_
- `to_include <https://github.com/DrSerpent/DrSerpent-Core/blob/master/DOCUMENTATION.md#to_include>`_
- `to_not_include <https://github.com/DrSerpent/DrSerpent-Core/blob/master/DOCUMENTATION.md#to_not_include>`_
- `to_output_to_stdout <https://github.com/DrSerpent/DrSerpent-Core/blob/master/DOCUMENTATION.md#to_output_to_stdout>`_
- `to_throw_error <https://github.com/DrSerpent/DrSerpent-Core/blob/master/DOCUMENTATION.md#to_throw_error>`_

Contributors:
=============

- `Alex McCarroll <https://github.com/AlexMcCarroll>`_
- `Ricky Hewitt <https://github.com/rewitt94>`_
- `Tom Betts <https://github.com/T-Betts>`_
- `Hemesh Unka <https://github.com/Hemesh-Unka>`_

How to contribute to this project:
==================================

See `CONTRIBUTING.md <https://github.com/DrSerpent/DrSerpent-Core/blob/master/CONTRIBUTING.md>`_

Licence:
========

Distributed under the terms of the `MIT <https://github.com/DrSerpent/DrSerpent-Core/blob/master/LICENSE.txt>`_ license, DrSerpent is free and open source software.
