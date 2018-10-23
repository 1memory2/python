shapes = [Ellipse(10,20), Square(15), Circle(5), Rectangle(20,15), Circle(5), Square(15), Ellipse(10,20)] 
areas = [x.area for x in shapes]
print('areas: ', areas)
total_area = sum(areas)
print('total_area: ', total_area)
