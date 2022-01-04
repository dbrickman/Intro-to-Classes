class Animal:
    """Animal Class"""
    def __init__(self, name, group, species, location, age=0 ):
        print('Creating animal')
        self.__name = name
        self.__group = group
        self.__species = species
        self.__location = location        
        self.__age = age

    @property
    def name(self):
        print('Getting name')
        return self.__name
    
    @property
    def group(self):
        print('Getting group')
        return self.__group

    @property
    def species(self):
        print('Getting species')
        return self.__species

    @property
    def location(self):
        print('Getting location')
        return self.__location

    @property
    def age(self):
        print('Getting age')
        return self.__age

    @name.setter
    def name(self, new_name):
        print('Setting name')
        self.__name = new_name

    @group.setter
    def group(self, new_group):
        print('Setting group')
        self.__group = new_group

    @species.setter
    def species(self, new_species):
        print('Setting species')
        self.__species = new_species

    @location.setter
    def location(self, new_location):
        print('Setting location')
        self.__location = new_location

    @age.setter
    def age(self, new_age):
        print('Setting age')
        self.__age = new_age

    def move(self):
        print('Moving')

    def eat(self):
        print('Eating')

    def sleep(self):
        print('Sleeping')

class Book():
    """Book Class"""

    def __init__(self, title, author, length, publisher, date_published, genre):
        print('Creating book')
        self.__title = title
        self.__author = author
        self.__length = length
        self.__publisher = publisher
        self.__date_published = date_published
        self.__genre = genre

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def length(self):
        return self.__length

    @property
    def publisher(self):
        return self.__publisher

    @property
    def date_published(self):
        return self.__date_published

    @property
    def genre(self):
        return self.__genre

    @title.setter
    def title(self, new_title):
        self.__title = new_title

    @author.setter
    def author(self, new_author):
        self.__author = new_author

    @length.setter
    def length(self, new_length):
        self.__length = new_length

    @publisher.setter
    def publisher(self, new_publisher):
        self.__publisher = new_publisher

    @date_published.setter
    def date_published(self, new_date_published):
        self.__date_published = new_date_published

    @genre.setter
    def genre(self, new_genre):
        self.__genre = new_genre
    
    def open():
        print('Opening book')

    def turn_page():
        print('Turning the page')

    def close():
        print('Closing book')
    

class Vehicle():
    """Vehicle Class"""

    def __init__(self, make, model, year, mileage, exterior_color, interior_color, location, move_type):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__mileage = mileage
        self.__exterior_colore = exterior_color
        self.__interior_color = interior_color
        self.__location = location
        self.__move_type = move_type
    
    @property
    def make(self):
        return self.__make

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    @property
    def mileage(self):
        return self.__mileage

    @property
    def exterior_color(self):
        return self.__exterior_colore

    @property
    def interior_color(self):
        return self.__interior_color

    @property
    def location(self):
        return self.__location

    @property
    def move_type(self):
        return self.__move_type

    @make.setter
    def make(self, new_make):
        self.__make = new_make

    @model.setter
    def model(self, new_model):
        self.__model = new_model

    @year.setter
    def year(self, new_year):
        self.__year = new_year

    @mileage.setter
    def mileage(self, new_mileage):
        self.__mileage = new_mileage

    @exterior_color.setter
    def exterior_color(self, new_exterior_color):
        self.__exterior_colore = new_exterior_color

    @interior_color.setter
    def interior_color(self, new_interior_color):
        self.__interior_color = new_interior_color

    @location.setter
    def location(self, new_location):
        self.__location = new_location

    @move_type.setter
    def move_type(self, new_move_type):
        self.__move_type = new_move_type

    def move():
        print('Vehicle is moving')

    def stop():
        print('Vehicle is stopped')