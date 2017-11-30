objective = 4
coins = [1,2,5,10,20,50,100,200]
ways = [(),[[1]]] + [[] for _ in xrange(objective-1)]
for i in xrange(2,objective+1):
    previous_solutions = ways[i-1]
    current_solutions = ways[i]
    print "finding new solutions for", i
    print "previous solutions:", previous_solutions
    print "current solutions:", current_solutions
    print id(current_solutions) == id(previous_solutions)
    for solution in previous_solutions:
        print "solution:", solution
        current_solutions.append(solution+[1])
        this_solution = current_solutions[-1]
        for j in xrange(len(this_solution)):
            grouped_subsolution = sum(this_solution[:j])
            if grouped_subsolution in coins: 
                new_solution = [grouped_subsolution] + this_solution[j:]
                if new_solution not in current_solutions:
                    current_solutions.append(new_solution)
                    print "added new:", new_solution, current_solutions

    

print ways[-1]



