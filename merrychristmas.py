print(*(l.center(21) for l in ('*',*(''.join('o#'[i%2] for i in range(c)) for c in range(3,22,2)),'/|\\')), sep='\n')

