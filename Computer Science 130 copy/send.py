


from cs1graphics import*
paper = Canvas(300,200, 'skyBlue', 'My World')

sun = Circle(30, Point(250,50))
sun.setFillColor('yellow')
paper.add(sun)

facade = Square(60, Point(140,130))
facade.setFillColor('white')
paper.add(facade)

chimney = Rectangle(15, 28, Point(155,85))
chimney.setFillColor('red')
chimney.setBorderColor('red')
paper.add(chimney)

tree = Polygon(Point(50,80), Point(30,140), Point(70,140))
tree.setFillColor('darkGreen')
paper.add(tree)

trunk = Rectangle(20, 35, Point(50, 157))
trunk.setFillColor('brown')
paper.add(trunk)

smoke = Path(Point(155,70), Point(150,65),
Point(160,55), Point(155,50))
paper.add(smoke)

grass = Rectangle(300,80, Point(150,160))
grass.setFillColor('green')
grass.setBorderColor('green')
grass.setDepth(75)
paper.add(grass)

window = Rectangle(15,20, Point(130,120))
paper.add(window)
window.setFillColor('black')
window.setBorderColor('red')
window.setBorderWidth(2)
window.setDepth(30)

roof = Polygon(Point(105,105), Point(175,105), Point(170,85), Point(110,85))
roof.setFillColor('darkgray')
roof.setDepth(30)
chimney.setDepth(20)
paper.add(roof)

paper.remove(smoke)

trunk = Rectangle(20, 35, Point(50, 157))
trunk.setFillColor('brown')
paper.add(trunk)

sand = Rectangle(300,80, Point(150,160))
sand.setFillColor('tan')
sand.setBorderColor('tan')
sand.setDepth(75)
paper.add(sand)

lake = Polygon(Point(200, 200), Point(275,200), Point(250,120), Point(230,120))
lake.setFillColor('darkblue')
lake.setDepth(30)
paper.add(lake)
