length = 5

for i in range(length):
    print(i)


financials = {      # Dict is Py equivalent of Java #Map
    "Q1" : {"revenue" : 50, "expense" : 10},
    "Q2" : {"revenue" : 52, "expense" : 11},
    "Q3" : {"revenue" : 53, "expense" : 12}
}

for quarter, data in financials.items():
    print(f"Quarter : {quarter} Financials : {data}")
    margin = (data['revenue'] - data['expense'])*100/data['revenue']
    print(f"Margin : {margin:2.2f}%")


#   Tuple
purple = (128, 0, 0)
yellow = (255, 255, 0)
r, g, b = purple
print(r, g, b)

mixture = ((purple[0] + yellow[0])//2, (purple[1] + yellow[1])//2, (purple[2] + yellow[2])//2)

print(mixture)


def calculate_profit_and_margin(revenue: int, expense: int) -> tuple[int, float]:
    profit = revenue - expense
    margin = profit * 100 / revenue
    return profit, margin

for quarter, data in financials.items():
    profit, margin = calculate_profit_and_margin(data['revenue'], data['expense'])
    print(f"Profit -> {profit}  Margin -> {margin:2.2f}")

def calc_args(*args):
    print(args)
    print(sum(args))

def calc_kwargs(**kwargs):
    print(kwargs)
    tot =0
    for item in kwargs.items():
        if isinstance(item[1], int):
            tot += item[1]
    print(tot)


calc_args(1, 2, 3, 4, 5, 6)
calc_kwargs(One = 1, Two = 2, Three=3, Four = '4')