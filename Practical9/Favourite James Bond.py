def find(y):
    y_18=y+18
    if 1962<=y_18<1973:
        return 	'Sean Connery'
    elif 1973<=y_18<=1986:
        return 	'Roger Moore'
    elif 1987<=y_18<=1994:
        return 	'TimothyDalton'
    elif 1995<=y_18<=2005:
        return  'Pierce Brosnan'
    elif 2006<=y_18<=2021:
        return   'Daniel Craig'

favorite_bond = find(1990)
print(favorite_bond)