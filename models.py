from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime
engine = create_engine('sqlite:///temperatures.db', echo=True)
meta = MetaData()

temperatures = Table(
   'temperatures', meta,
   Column('id', Integer, primary_key=True, autoincrement=True),
   Column('sensor_id', Integer),
   Column('temperature', Integer),
   Column('timestamp', DateTime),
)


if __name__ == '__main__':
    meta.create_all(engine)
    print('database created')

