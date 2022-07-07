import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_table, Publisher, Book, Shop, Stock, Sale
import json


def create_db_table(engine):
    create_table(engine)

    with open('test_data.json') as f:
        json_data = json.load(f)
        
    Session = sessionmaker(bind=engine)
    session = Session()

    for data in json_data:
        table_name = {
            'publisher': Publisher, 'book': Book, 'shop': Shop, 'stock': Stock, 'sale': Sale
            }[data['model']]
        
        session.add(table_name(**data['fields']))
        session.commit()
        
    session.close()

def requests_publisher(engine):    
    
    id_publish = int(input('Введите идентификатор автора (всего 4): '))
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    for c in session.query(Book).join(Publisher.book).filter(Publisher.id == id_publish).all():
        print(c)
    
    
    session.close()
    
    


def main():
    # Объект подключения
    
    name_user = ''
    passdb = ''
    db = 'shop'
    
    
    DNS = f'postgresql://{name_user}:{passdb}@localhost:5432/{db}'
    engine= sqlalchemy.create_engine(DNS)
    
    # create_db_table(engine)
    
    requests_publisher(engine)



if __name__ == '__main__':
    main()