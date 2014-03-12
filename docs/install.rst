********
環境安裝
********

.. contents::
   :backlinks: none

Python 3.3
==========

我們這邊選擇自原始碼編譯。

Mac
---

推薦使用 Homebrew 套件管理安裝。

.. code-block:: bash

    brew install python3

Cent 6
------

.. code-block:: bash

    sudo yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel db4-devel
    wget http://python.org/ftp/python/3.3.2/Python-3.3.2.tar.xz
    # 不能解壓縮 *.tar.xz 格式的話請另安裝 xz-devel
    tar Jxvf Python-3.3.2.tar.xz
    cd Python-3.3.2
    ./configure
    make
    sudo make install

.. warning:: Cent 5 無法通過所有 Python 3 測試，需要自行更新 c lib，不建議安裝！

Ubuntu
------

.. code-block:: bash

    sudo apt-get install libncursesw5-dev libreadline-dev libssl-dev libgdbm-dev libc6-dev libsqlite3-dev tk-dev
    wget http://python.org/ftp/python/3.3.2/Python-3.3.2.tar.xz
    # 不能解壓縮 *.tar.xz 格式的話請另安裝 xz-utils
    tar Jxvf Python-3.3.2.tar.xz
    cd Python-3.3.2
    ./configure
    make
    sudo make install

.. note:: ``sudo apt-get python3`` 目前沒有測試，不敢保証。但這樣建議一定要使用 virtualenv


Setuptools & Pip
================

Mac
---
Homebrew 安裝完後就有 setuptools。

Cent 6 & Ubuntu
---------------

.. code-block:: bash

    wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py
    sudo python3 ez_setup.py
    sudo easy_install-3.3 pip


__ http://brew.sh/


.. code-block:: bash

    brew install python3


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
------------------------------

虛擬環境的目錄很可能會散落在系統四處，多起來有時不易管理。尤其是目錄往往與程式碼分開。Virtualenvwrapper 主要幫助簡化常用的 virtualenv 操作。

.. code-block:: bash

    sudo pip3 install virtualenvwrapper

Managing multiple environments is not easy. ``virtualenvwrapper`` helps to do this job.

For supporting Python 3.x, after the installaion, one should add environemnt variable to the shell as follows::

    # For virtualenvwrapper settings
    export WORKON_HOME=$HOME/MyEnvs
    export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3.3
    export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv-3.3
    source /usr/local/bin/virtualenvwrapper_lazy.sh

They could be placed in somewhere like ``~/.bash_profile`` or ``~/.zshrc``, which path to Python 3.x and virtualenv should be properly set. For more configuration please visit their official site.

Usage is easy. Make a new virtualenv is easy.

.. code-block:: bash

    mkvirtualenv LAB_SOS

Options to virtualenv can be passed in the same way.

.. code-block:: bash

    mkvirtualenv -p /usr/local/bin/python2.7 LAB_SOS-27

Enter a virtual environment at any location

.. code-block:: bash

    workon LAB_SOS

Leave the virtual environment in the same way.

.. code-block:: bash

    deactivate
