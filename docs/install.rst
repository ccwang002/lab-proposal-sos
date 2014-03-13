********
環境安裝
********

Python 版本與開發環境套件
=========================

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

    brew install python3
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


pyenv 管理多版本 Python
=======================

用法同 rbenv。方便做不同 Python 版本間切換與開發。

.. seealso:: 小弟在 Python\@ptt1 的文章 `pyenv + Py3.4 + numpy 在 OSX 10.9`__

__ http://www.ptt.cc/bbs/Python/M.1390807436.A.7F7.html

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

    They could be placed in somewhere like ``~/.bash_profile`` or ``~/.zshrc``,
    where the path to Python 3.x and virtualenv should be properly set.
    For more configuration please visit their official site.

Usage is easy. Make a new virtualenv is two words away.
Folders for these virtual environment are created under  ``$WORKON_HOME``::

    mkvirtualenv LAB_SOS

Options to virtualenv can be passed directly to mkvirtualenv::

    mkvirtualenv --system-site-packages LAB_SOS_SYS

Activating a virtual environment at any location is trivial::

    workon LAB_SOS

Leave the virtual environment as usual::

    deactivate
