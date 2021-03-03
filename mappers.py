import sqlite3

from models import Student, Category

connection = sqlite3.connect('site_db.sqlite')


class RecordNotFoundException(Exception):
    def __init__(self, text):
        super().__init__(f'Record not found: {text}')


class DBCommitException(Exception):
    def __init__(self, text):
        super().__init__(f'DB commit error: {text}')


class DBUpdateException(Exception):
    def __init__(self, text):
        super().__init__(f'DB update error: {text}')


class DBDeleteException(Exception):
    def __init__(self, text):
        super().__init__(f'DB delete error: {text}')


class StudentMapper:

    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()
        self.table_name = 'student'

    def find_all(self):
        command = f'SELECT * FROM {self.table_name}'
        self.cursor.execute(command)
        result = []
        for item in self.cursor.fetchall():
            id, name = item
            student = Student(name)
            student.id = id
            result.append(student)
        return result

    def find_by_id(self, id):
        command = f'SELECT id, name FROM {self.table_name} WHERE id=?'
        self.cursor.execute(command, (id,))
        result = self.cursor.fetchone()
        if result:
            return Student(*result)
        else:
            raise RecordNotFoundException(f'запись с id={id} не найдена')

    def find_by_name(self, name):
        command = f'SELECT id, name FROM {self.table_name} WHERE id=?'
        self.cursor.execute(command, (id,))
        result = self.cursor.fetchone()
        if result:
            return Student(*result)
        else:
            raise RecordNotFoundException(f'запись с id={id} не найдена')

    def insert(self, obj):
        command = f'INSERT INTO {self.table_name} (name) VALUES (?)'
        self.cursor.execute(command, (obj.name,))
        try:
            self.connection.commit()
        except Exception as e:
            raise DBCommitException(e.args)

    def update(self, obj):
        command = f'UPDATE {self.table_name} SET name=? WHERE id=?'
        self.cursor.execute(command, (obj.name, obj.id))
        try:
            self.connection.commit()
        except Exception as e:
            raise DBUpdateException(e.args)

    def delete(self, obj):
        command = f"DELETE FROM {self.table_name} WHERE id=?"
        self.cursor.execute(command, (obj.id,))
        try:
            self.connection.commit()
        except Exception as e:
            raise DBDeleteException(e.args)


class MapperRegistry:
    mappers = {
        'student': StudentMapper,
        # 'category': CategoryMapper
    }

    @staticmethod
    def get_mapper(obj):
        if isinstance(obj, Student):
            return StudentMapper(connection)
        # if isinstance(obj, Category):
        #     return CategoryMapper(connection)

    @staticmethod
    def get_current_mapper(name):
        return MapperRegistry.mappers[name](connection)