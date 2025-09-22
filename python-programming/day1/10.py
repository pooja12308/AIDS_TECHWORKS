#Convert days to years and months
def convert(days):
    years=days/365
    months=days/30
    print(round(years))
    print(round(months))
days=440
convert(days)