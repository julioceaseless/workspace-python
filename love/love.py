#!/usr/bin/python3
""" draws a heart with a message"""


def show_love(message):
  print('\n'.join
    ([''.join
      ([(f' {message}  '[(x-y)%(len(message) + 2) ]
        if((x*0.04)**2 + (y*0.1)**2-1)
          **3-(x*0.05)**2*(y*0.1)
            **3<=0 else ' ')
              for x in range(-30, 40)])
                for y in range(20, -15, -1)]))
  print("\t\t    Happy Women's Day!!\n\n")
show_love("Happy Women's Day")
