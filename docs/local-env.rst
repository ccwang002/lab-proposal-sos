******************
在本機設定開發環境
******************

可以分成以下幾個步驟，請自己跳過完成的部份：

#. 建立 Virtualenv 環境，安裝套件

   .. code-block:: bash

        $ virtualenv venv
        # ...
        # Also creating executable in venv/bin/python
        # Installing setuptools, pip...done.
        $ source venv/bin/activate
        (venv) $ pip install -r requirements.txt
        # 安裝各套件…

#. 建立 db

   .. code-block:: bash

        $ python lab_sos.py shell
        >>> from lab_sos import db
        >>> db.drop_all()    # 移除以前的資料表
        >>> db.create_all()  # 初始化

   可以使用 ``$ sqlite3 data.sqlite .schema`` 來檢查資料表有沒有建立

#. 起動開發用 server

   .. code-block:: bash

        $ python lab_sos.py runserver
        # * Running on http://127.0.0.1:5000/
        # * Restarting with reloader
