from ..model.base.base_model import BaseModel


class TimeRegistrationConfig(BaseModel):
    def __init__(self,name=None, start_date=None, start_time=None, preparation_duration=None, standup_duration=None,
                 time_registration_duration=None):
        super().__init__()
        self.name = name
        self.start_date = start_date
        self.start_time = start_time
        self.preparation_duration = preparation_duration
        self.standup_duration = standup_duration
        self.time_registration_duration = time_registration_duration

    def store(self):
        query = 'INSERT INTO time_registration_configs (name, start_date, start_time, preparation_duration,' \
                ' standup_duration, time_registration_duration) VALUES (%s, %s, %s, %s, %s, %s)'
        val = (self.start_date, self.start_time, self.preparation_duration, self.standup_duration,
               self.time_registration_duration)
        try:
            with self.db_connection.cursor() as cursor:
                cursor.execute(query, val)
                self.db_connection.commit()
                self.id = cursor.lastrowid
        except Exception as e:
            print(f"An error occurred: {e}")

    def update(self):
        query = 'UPDATE time_registration_configs SET name = %s, start_date = %s, start_time = %s, preparation_duration' \
                ' = %s, standup_duration = %s, time_registration_duration = %s WHERE id = %s'
        val = (self.start_date, self.start_time, self.preparation_duration, self.standup_duration,
               self.time_registration_duration, self.id)

        try:
            with self.db_connection.cursor() as cursor:
                cursor.execute(query, val)
                self.db_connection.commit()
        except Exception as e:
            print(f"An error occurred: {e}")

    def get_by_id(self, id):
        query = 'SELECT name, start_date, start_time, preparation_duration,' \
                ' standup_duration, time_registration_duration FROM time_registration_configs WHERE id = %s'

        try:
            with self.db_connection.cursor() as cursor:
                cursor.execute(query, (id,))
                result = cursor.fetchone()
                if result:
                    return TimeRegistrationConfig(start_date=result[0], start_time=result[1],
                                                  preparation_duration=result[2], standup_duration=result[3],
                                                  time_registration_duration=result[4])
                else:
                    return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def get_all(self):
        query = 'SELECT id, name, start_date, start_time, preparation_duration,' \
                ' standup_duration, time_registration_duration FROM time_registration_configs'

        try:
            with self.db_connection.cursor() as cursor:
                cursor.execute(query)
                results = cursor.fetchall()
                return [TimeRegistrationConfig(start_date=row[1], start_time=row[2],
                                               preparation_duration=row[3], standup_duration=row[4],
                                               time_registration_duration=row[5])
                        for row in results]
        except Exception as e:
            print(f"An error occurred: {e}")
            return []
