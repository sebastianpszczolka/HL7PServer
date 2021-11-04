from lib.core.conf import Conf, ConfParam


class AppConf(Conf):
    def __init__(self, filename: str):
        """

        :param filename: configuration file name
        """

        super().__init__(filename)

        self.server_port = ConfParam('SERVER', 'port', def_val=8091, type_val=int)
        self.db_host = ConfParam('DATABASE', 'host', def_val='localhost')
        self.db_name = ConfParam('DATABASE', 'name', def_val='medic')
        self.db_user = ConfParam('DATABASE', 'user', def_val='client1')
        self.db_passwd = ConfParam('DATABASE', 'password', def_val='client1')
        self.db_port = ConfParam('DATABASE', 'port', def_val=5432, type_val=int)

        self.cfg_array.extend(
            [self.server_port, self.db_host, self.db_name, self.db_user, self.db_passwd, self.db_port])
