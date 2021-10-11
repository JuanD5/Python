from nearest import nearest_square

# Test files always have to start with the name "test_"
def test_nearest_square_5():
    assert (nearest_square(5)==4)
    
def test_nearest_square_12():
    assert (nearest_square(-12)==0)
    
def test_nearest_square_9():
    assert (nearest_square(9)==9)
    
def test_nearest_square_23():
    assert (nearest_square(23)==16)            