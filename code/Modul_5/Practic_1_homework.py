def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

test_function()
# inner_function() - функция существует только внутри локального пространства test_function, поэтому она не может отобразиться в глобальном пространстве
