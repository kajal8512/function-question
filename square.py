def val_power(exponent):
    def pow_of(base):
        return pow(base,exponent)
    return pow_of
square=val_power(2)
print(square(5))