good = r"""
     __/)     (\__
  ,-'~~(   _   )~~`-.
 /      \/'_`\/      \
|       /_(_)_\       |
|     _(/(\_/)\)_     |
|    / // \ / \\ \    |
 \  | ``  / \ ''  |  /
  \  )   /   \   (  /
   )/   /     \   \(
   '    `-`-'-'    `
unknown
"""
bad = r"""
        /)
   .-"".L,""-.
  ;       :.  :
  (       7:  )
   :         ;
ctr "..-"-.."
"""
drawbridge_raised = True
if not drawbridge_raised:
    outcome = "Thunder: The drawbridge is down you can safely walk to freedom"
    print(good)
else:
    outcome = "Doom: The drawbridge is up and there is no way of getting to freedom"
    print(bad)
print(outcome)