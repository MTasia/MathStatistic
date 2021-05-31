from bivariate_normal import b_normal


class norm_sample_2d:
    _data = []
    __size = 0
    __cor_coeff = None
    __x_mean = None
    __y_mean = None
    __x_div = None
    __y_div = None

    def __init__(self, x_mean, y_mean, x_div, y_div, cor_coef: float, size):
        self.__cor_coeff = cor_coef
        self.__x_mean = x_mean
        self.__y_mean = y_mean
        self.__x_div = x_div
        self.__y_div = y_div
        self.__data = b_normal(x_mean, y_mean, x_div, y_div, cor_coef, size)
        self.__size = size

    def get_size(self):
        return self.__size

    def get_data(self):
        return self.__data

    def get_cor_coef(self):
        return self.__cor_coeff

    def get_x_mean(self):
        return self.__x_mean

    def get_y_mean(self):
        return self.__y_mean

    def get_x_div(self):
        return self.__x_div

    def get_y_div(self):
        return self.__y_div
