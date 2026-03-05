good = r"""
                          *  *       *  * 
                        *      *   *      *
                        *       * *       *
                         *       *       *   
                           *           *
                             *       *
                               *   *
                                * *             arm
                                 *
 """
bad = r"""
                .---.   .---.
              ,';'   `.';'   `..
              f               :Bo.
              `               d88:
               `\           /d88P'
                 `\     ; /d888P'
                   `.  ',d8&8P'
                     : ;d8&7'
                      | :8:
                         |  qx
"""
guard_awake = True
if not guard_awake:
    outcome = "Shadow: the guard is sleeping you can pass by safely "
    print(good)
else:
    outcome = "Doom: The guard spots you and you are killed"
    print(bad)
print(outcome)