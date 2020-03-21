

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

result = []
for filename in filenames:
    if filename.endswith(".hpp"):
        result.append("({}, {})".format(filename, filename[:-2]))
    else:
        result.append("({}, {})".format(filename, filename))

print(result) # Should be [('program.c', 'program.c'), ('stdio.hpp', 'stdio.h'), ('sample.hpp', 'sample.h'), ('a.out', 'a.out'), ('math.hpp', 'math.h'), ('hpp.out', 'hpp.out')]
