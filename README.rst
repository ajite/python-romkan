.. image:: https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/ajite/c90a126b4e926b94c07a36ac78e9a9ad/raw/python-romkan-ng_coverage.json
	:target: https://github.com/ajite/python-romkan-ng
	:alt: Coverage

python-romkan-ng
================

Fork of `python-romkan <https://github.com/soimort/python-romkan/>`_

`python-romkan-ng <https://github.com/soimort/python-romkan>`_ works on Python 3.9 and above. It handles both Katakana (片仮名) and Hiragana (平仮名) with the Hepburn (ヘボン式) romanization system, as well as the modern Kunrei-shiki (訓令式) romanization system.

Installation
------------

Install via pip:
~~~~~~~~~~~~~~~~

.. code-block:: bash

    pip install romkan-ng

Install from Git:
~~~~~~~~~~~~~~~~~

.. code-block:: bash

    git clone git://github.com/ajite/python-romkan-ng.git
    poetry install



Usage
-----

Python 3.x::

    $ python
    >>> import romkan
    >>> print(romkan.to_roma("にんじゃ"))
    ninja
    >>> print(romkan.to_hepburn("にんじゃ"))
    ninja
    >>> print(romkan.to_kunrei("にんじゃ"))
    ninzya
    >>> print(romkan.to_hiragana("ninja"))
    にんじゃ
    >>> print(romkan.to_katakana("ninja"))
    ニンジャ


API Reference
-------------

* **to_katakana(string)**

Convert a Romaji (ローマ字) to a Katakana (片仮名).

* **to_hiragana(string)**

Convert a Romaji (ローマ字) to a Hiragana (平仮名).

* **to_kana(string)**

Convert a Romaji (ローマ字) to a Katakana (片仮名). (same as *to_katakana*)

* **to_hepburn(string)**

Convert a Kana (仮名) or a Kunrei-shiki Romaji (訓令式ローマ字) to a Hepburn Romaji (ヘボン式ローマ字).

* **to_kunrei(string)**

Convert a Kana (仮名) or a Hepburn Romaji (ヘボン式ローマ字) to a Kunrei-shiki Romaji (訓令式ローマ字).

* **to_roma(string)**

Convert a Kana (仮名) to a Hepburn Romaji (ヘボン式ローマ字).



License
-------

`python-romkan <https://github.com/ajite/python-romkan-ng>`_ is licensed under the `BSD license <https://raw.github.com/ajite/python-romkan-ng/master/LICENSE>`_.
