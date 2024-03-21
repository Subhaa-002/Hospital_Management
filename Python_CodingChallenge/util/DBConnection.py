import pyodbc
class DBConnection:
    connection = None

    @staticmethod
    def getConnection():
        if DBConnection.connection is None:
                try:
                    connection = pyodbc.connect('Driver={SQL Server};'
                                          'Server=MS\SQLEXPRESS01;'
                                          'Database=Hospital;'
                                          'Trusted_Connection=yes;')
                except:
                    print("Connection failed")

        return connection

