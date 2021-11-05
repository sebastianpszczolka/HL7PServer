from lib.core.log import LogMixin
import psycopg2


class DB(LogMixin):
    def __init__(self, host: str, db_name: str, user: str, passwd: str, port: int):
        self.host = host
        self.db_name = db_name
        self.user = user
        self.passwd = passwd
        self.port = port

    def save_simple_text_record(self, record: str):
        """

        :param record:
        :return:
        """

        self.logger.info(f'Save record: {record}')

        sql = """INSERT INTO public.t_record (r_record) VALUES (%s);"""

        connection = None
        cursor = None
        try:
            connection = psycopg2.connect(user=self.user,
                                          password=self.passwd,
                                          host=self.host,
                                          port=self.port,
                                          database=self.db_name,
                                          connect_timeout=1)

            cursor = connection.cursor()
            cursor.execute(sql, (record,))
            connection.commit()
            count = cursor.rowcount
            print(count, "Record inserted successfully into mobile table")

        except:
            self.logger.exception("DB->save_simple_text_record")
        finally:

            if connection:
                if cursor:
                    cursor.close()
                connection.close()
