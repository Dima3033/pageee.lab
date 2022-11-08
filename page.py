try:
    num = input(' Enter pages -> ')
    sym = input("sym ->")
    print(f'count = {num.count(sym)}')
except Exception as ex:
   print(f'Erorr information: {ex}')