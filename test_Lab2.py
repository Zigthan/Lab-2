import Lab2 

def test_find_min_max_temperature():
    result =[]
    input_list = [5, 67, 32, 15, 89, 23, 41]
    expected_result = (5, 89)

    result = Lab2.find_min_max_temperature(input_list)

    assert result == expected_result

def test_calc_average_temperature():
    result = 0
    input_list = [10, 20, 30, 40, 50]
    expected_result = 30.0

    result = Lab2.calc_average_temperature(input_list)

    assert result == expected_result
def test_calc_median_temperature():
    result = 0
    input_list = [5, 10, 15, 20, 25, 30, 35]
    expected_result = 20.0

    result = Lab2.calc_median_temperature(input_list)

    assert result == expected_result