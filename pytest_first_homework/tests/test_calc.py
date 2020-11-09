from pytest_first_homework.core.calc import Calc
import pytest

class TestCalc:
    def setup_class(self):
        self.calc = Calc()
    #正常值(整数），测试除法
    @pytest.mark.parametrize('a,b,c',[
        [10,2,5],
        [-10,2,-5],
        [10,-2,-5],
        [-10,-2,5]
    ])
    def test_div_1(self,a,b,c):
        '''正常值(整数），测试除法'''
        assert self.calc.div(a,b) == c

    #正常值(浮点数+整数除不尽），测试除法
    @pytest.mark.parametrize('a,b,c',[
        [6.34,2.24,2.83],
        [-6.34,2.24,-2.83],
        [6.34,-2.24,-2.83],
        [-6.34,-2.24,2.83],
        [10,3,3.33],
        [-10,3,-3.33],
        [10,-3,-3.33],
        [-10,-3,3.33]
    ])
    def test_div_2(self,a,b,c):
        '''正常值(浮点数+整数除不尽），测试除法'''
        assert round(self.calc.div(a,b),2) == c

    #正常值(除数为0），测试除法
    @pytest.mark.parametrize('a,b,c',[
        [0,5,0],
        [0,-5,0],
        [0,-2.24,0],
        [0,2.24,0]
    ])
    def test_div_3(self,a,b,c):
        '''正常值(除数为0），测试除法'''
        assert self.calc.div(a,b) == c

    #异常值(被除数为0+除数、被除数中含非数字字符），测试除法
    @pytest.mark.parametrize('a,b',[
        [0,0],
        [5,0],
        [-5,0],
        [5.34,0],
        [-5.34,0],
        ['a',0],
        ['a',2],
        ['a','b'],
        [3,'a'],
        [0,'a']
    ])
    def test_div_4(self,a,b):
        '''异常值(被除数为0+除数、被除数中含非数字字符），测试除法'''
        with pytest.raises(Exception):
            assert self.calc.div(a,b) == 0

    @pytest.mark.parametrize('a,b,c',[
        [3,5,15],
        [-3,5,-15],
        [3,-5,-15],
        [-3,-5,15]
    ])
    def test_mul_1(self,a,b,c):
        '''正常值（整数），测试乘法'''
        assert self.calc.mul(a,b) == c

    @pytest.mark.parametrize('a,b,c',[
        [3.23,5.45,17.60],
        [-3.23,5.45,-17.60],
        [3.23,-5.45,-17.60],
        [-3.23,-5.45,17.60],
        [2,4.45,8.90],
        [-2,4.45,-8.90],
        [2,-4.45,-8.90],
        [-2,-4.45,8.90],
    ])
    def test_mul_2(self,a,b,c):
        '''正常值（浮点数），测试乘法'''
        assert round(self.calc.mul(a,b),2) == c

    @pytest.mark.parametrize('a,b,c', [
        [0, 5, 0],
        [3, 0, 0],
        [0, -5, 0],
        [-3, 0, 0],
        [4.54, 0, 0],
        [0, 4.54, 0],
        [0,0,0]
    ])
    def test_mul_3(self,a,b,c):
        '''正常值（含有0），测试乘法'''
        assert self.calc.mul(a,b) == c

    @pytest.mark.parametrize('a,b,c',[
        [5,'a','aaaaa'],
        ['a',5,'aaaaa']
    ])
    def test_mul_4(self,a,b,c):
        '''正常值（含有一个字母），测试乘法'''
        assert self.calc.mul(a,b) == c

    @pytest.mark.parametrize('a,b',[
        ['a','b'],
        [-5,'a'],
        ['a',-5]
    ])
    def test_mul_5(self,a,b):
        '''异常值（含有非数字），测试乘法'''
        with pytest.raises(Exception):
            assert self.calc.mul(a,b)

    #逻辑测试(正常）
    @pytest.mark.parametrize('a,b,d,e',[
        [10,2,5,25]
    ])
    def test_process_1(self,a,b,d,e):
        '''逻辑测试(正常）'''
        c = self.calc.div(a,b)
        assert self.calc.mul(c,d) == e

    #逻辑测试(非正常）
    @pytest.mark.parametrize('a,b,d,e',[
        [10,2,5,25]
    ])
    def test_process_2(self,a,b,d,e):
        '''逻辑测试(非正常）'''
        c = self.calc.mul(a,b)
        with pytest.raises(Exception):
            assert self.calc.div(c,d) == e