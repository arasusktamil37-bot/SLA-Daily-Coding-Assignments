#Laptop Information: Create a Laptop class with brand, processor, RAM, and storage. Initialize the attributes and display the laptop configuration.
class Laptop:
  def __init__(self,Brand,Processor,RAM,Storage):
    self.Brand = Brand
    self.Processor = Processor
    self.RAM = RAM
    self.Storage = Storage

  def display(self):
    print(f" MY LAPTOP IS A {self.Brand} BRAND WITH {self.Processor} PROCESSOR AND WITH {self.RAM} RAM AND HAS A STORAGE OF {self.Storage}" )

objectlaptop = Laptop("LENOVO","INTEL 5","16GB","512 SSD")
objectlaptop.display()

#Product Details: Create a Product class with product ID, product name, quantity, and price. Create an object and display the product details.

class Product:
  def __init__(self,Product_id,Product_name,Quantity,Price):
    self.Product_id = Product_id
    self.Product_name = Product_name
    self.Quantity = Quantity
    self.Price = Price

  def show(self):
    print(f"I BOUGHT A {self.Product_name} WITH THE ID OF {self.Product_id} AND I BOUGHT {self.Quantity} OF THAT WHICH COST AROUND {self.Price}")

objectproduct = Product("116","WATERBOTTLE","7","7000")
objectproduct.show()

#Movie Information: Create a Movie class with movie name, director, language, and release year. Initialize and display the movie information.

class Movie :
  def __init__(self,Movie_name,Director,Language,Release_year):
    self.Movie_name = Movie_name
    self.Director = Director
    self.Language = Language
    self.Release_year = Release_year

  def give(self):
    print("MOVIE NAME : ",self.Movie_name)
    print("DIRECTOR NAME : ",self.Director)
    print("LANGUAGE OF THE MOVIE : ",self.Language)
    print("RELEASED YEAR ; ",self.Release_year)

watch = Movie("ODESSEY","CHRISTOFER NOLAN","ENGLISH","2026")
watch.give()

#Rectangle Details: Create a Rectangle class with length and breadth. Initialize both attributes and display the length, breadth, and calculated area.

class Rectangle:
  def __init__(self,Length,Breadth):
    self.Length = Length
    self.Breadth = Breadth

  def area(self):
    area = self.Length*self.Breadth
    print(area)
objectarea = Rectangle(3,3)
objectarea.area()
