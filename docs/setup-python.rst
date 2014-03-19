***************
Python 環境安裝
***************

Python 版本與最基本套件
=======================

- Python 3.3+
- (setuptools), pip
- virtualenv (強烈建議)


在 Ubuntu 13.10
---------------

.. code-block:: bash

    sudo apt-get install python3.3-dev
    sudo apt-get install python3-pip
    sudo pip3 install virtualenv

.. note:: Ubuntu 12.10+ 即可以使用 ``apt-get`` 方式安裝 3.3，但細節可能略為不同


在 CentOS 6
-----------

.. code-block:: bash

    # compile Python 3.3
    sudo yum install openssl-devel ncurses-devel sqlite-devel\
        readline-devel tk-devel db4-devel\
        zlib-devel bzip2-devel xz-devel
    wget http://python.org/ftp/python/3.3.4/Python-3.3.4.tar.xz
    tar Jxvf Python-3.3.4.tar.xz
    cd Python-3.3.4
    ./configure --enable-shared
    make
    sudo make install

    # install pip, virtualenv
    curl https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py | sudo python3
    sudo easy_install-3.3 pip
    sudo pip3 install virtualenv

.. note:: CentOS 5 無法通過所有 Python 3 測試，需要自行更新 c lib，請搜尋相關文章


在 Mac OSX 10.7+
----------------

推薦 `Homebrew`__ 套件管理安裝。

__ http://brew.sh/


.. code-block:: bash

    brew install python3 --with-brewed-openssl
    pip3 install virtualenv


Virtualenv 使用方式
===================

它的概念就是會在本機端建立一個資料夾作為一個 Python 環境（這邊以 ``LAB_SOS`` 為例），
當你 source 這個環境的時候，virtualenv 會自動把 Python 相關的路徑都導到這個目錄底下，
所以之後安裝的套件都會跑到這個環境底下，達到與系統隔離的效果。
而且也不需要 root 權限。這個環境會一直持續到 ``deactivate`` 結束。

.. code-block:: bash

    $ virtualenv-3.3 LAB_SOS       # 建立新的虛擬環境
    Using base prefix '...'
    New python executable in test_venv/bin/python3
    Also creating executable in test_venv/bin/python
    Installing setuptools, pip...done.

    $ source LAB_SOS/bin/activate  # 進入環境

    (LAB_SOS)$ which pip3          # 命令提示增加 (...) 來辨識　
    /path/to/LAB_SOS/bin/pip3      # 此時相關的執行路徑會被導到虛擬環境底下

    (LAB_SOS)$ deactivate          # 脫離環境

    $ which pip3
    # /usr/local/bin/pip3 or /usr/bin/pip3 為系統的 pip，路徑視安裝而定


VirtualenvWrapper *(Optional)*
==============================

虛擬環境的目錄很可能會散落在系統四處，多起來有時不易管理。
尤其是目錄往往與程式碼分開。virtualenvwrapper 主要幫助簡化常用的 virtualenv 操作。

.. note::
    以下示範的是一個最跨平台的做法，但在不同平台上可能有更好的解法。
    同時也不一定要用 virtualenvwrapper，像 fish shell 的 `virtual fish`_、
    或者 `pyenv-virtualenv`_ 與 `pyenv-virtualenvwrapper`_。

.. _`virtual fish`: https://github.com/adambrenecki/virtualfish
.. _`pyenv-virtualenv`: https://github.com/yyuu/pyenv-virtualenv
.. _`pyenv-virtualenvwrapper`: https://github.com/yyuu/pyenv-virtualenvwrapper


.. code-block:: bash

    pip3 install virtualenvwrapper

Managing multiple environments at different folders is bothering.
``virtualenvwrapper`` helps to do this job.

.. note::
    這是在 3.3 版還沒普及的時候寫的，現在可能不用這麼麻煩了。

    For supporting Python 3.x, after the installaion,
    one should add environemnt variable to the shell as follows::

        # For virtualenvwrapper settings
        export WORKON_HOME=$HOME/MyEnvs
        export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3.3
        export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv-3.3
        source /usr/local/bin/virtualenvwrapper_lazy.sh

    Place them in somewhere like ``~/.bash_profile`` or ``~/.zshrc``.

Usage is easy. Make a new virtualenv is two words away.
Folders for these virtual environment are created under  ``$WORKON_HOME``::

    mkvirtualenv LAB_SOS

Options to virtualenv can be passed directly to mkvirtualenv::

    mkvirtualenv --system-site-packages LAB_SOS_SYS

Activating a virtual environment at any location is trivial::

    workon LAB_SOS

Leave the virtual environment as usual::

    deactivate


pyenv 管理多版本 Python *(Optional)*
====================================

用法同 rbenv。方便做不同 Python 版本間切換與開發。如果沒有這個需求，請直接跳過此部份。

.. seealso::
    小弟在 Python\@ptt1 的文章 `[資訊] Python 3.4 released! + pyenv`__

__ http://www.ptt.cc/bbs/Python/M.1395145892.A.435.html


OS X
----

.. note::
    在 OS X ，pyenv 預設會連接系統內建的 library 如 sqlite3 與 openssl。
    但往往版本老舊，而且跟
    ``brew install python3 --with-brewed-openssl``
    的行為不同。雖然只是建立開發環境，仍請小心連結不同 library 帶來的差異。

    建議在使用 pyenv 安裝時，加入以下環境變數：

    .. code-block:: bash

        epoxrt CONFIGURE_OPTS="CC=clang"
        export CFLAGS="-I/usr/local/opt/openssl/include -I/usr/local/opt/sqlite/include"
        export LDFLAGS="-L/usr/local/opt/openssl/lib -L/usr/local/opt/sqlite/lib"

    再進行上述的安裝過程。可以用以下指令來檢查連結 libray 的版本：

    .. code-block:: bash

        # openssl
        `pyenv prefix 3.3.5`/bin/python -c "import ssl; print(ssl.OPENSSL_VERSION)"
        # sqlite3
        `pyenv prefix 3.3.5`/bin/python -c "import sqlite3 as s; print(s.sqlite_version_info)"


Vargrant for Devlopment Environment
===================================

計畫中，但不確定會不會做。
