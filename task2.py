good = r"""
    //_____ __
   @ )====// .\___
   \#\_\__(_/_\\_/
     / /       \\
Jiri Matejicek
"""
bad = r"""     _.,----,
   __  _.-._ / '-.        -  ,._  \) 
  |  `-)_   '-.   \       / < _ )/" }
  /__    '-.   \   '-, ___(c-(6)=(6)
   , `'.    `._ '.  _,'   >\    "  )
   :;;,,'-._   '---' (  ( "/`. -='/
  ;:;;:;;,  '..__    ,`-.`)'- '--'
  ;';:;;;;;'-._ /'._|   Y/   _/' \
        '''"._ F    |  _/ _.'._   `\
               L    \   \/     '._  \
        .-,-,_ |     `.  `'---,  \_ _|
        //    'L    /  \,   ("--',=`)7
       | `._       : _,  \  /'`-._L,_'-._
       '--' '-.\__/ _L   .`'         './/
                   [ (  /
                    ) `{
         snd        \__)
"""
has_key = True
if has_key:
    outcome = "Click: You find the key and you can open the door you are safe!!"
    print(good)
else:
    outcome = "Doom: There is no key you are stuck!!"
    print(bad)
print(outcome)