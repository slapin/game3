import os, pstats

count = 1
loop = True
while loop:
    filestr = str(count) + ".profile"
    try:
        open(filestr)
        count += 1
    except:
        loop = False
        
print filestr
    

os.system("python -m cProfile -o " + filestr + " main.py")

p = pstats.Stats(filestr)
p.strip_dirs()
p.sort_stats("cumulative")
p.print_stats(.02)
