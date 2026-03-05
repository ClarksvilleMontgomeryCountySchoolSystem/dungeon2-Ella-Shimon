good = r""" _|\ _/|_,
           ,((\\``-\\\\_
         ,(())      `))\
       ,(()))       ,_ \
      ((())'   |        \
      )))))     >.__     \
      ((('     /    `-. .c|
 hjw          /        `-`'
"""
bad = r"""
      
            (\_        _/)
          _." ';      .' "._
         /( )h\        (/( )\
  ctr___/  \|__        __|/  \__
"""
escaped = True
if escaped:
    outcome = "Legend: yayyy You are finally!! "
    print(good)
else:
    outcome = "Doom: You are cooked you are not getting out!!"
    print(bad)
print(outcome)