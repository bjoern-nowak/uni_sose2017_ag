from classes import DiGraph
from . import create_print_render_dot
from . import print_output_info


print("\nStart: Exercise 05 Task 19\n")
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

graph = DiGraph(title="Exercise 05 Task 19 Graph 01",
                filename="e05_t19_g01")
graph.read_input(value="a:f;b:a;c:a,e;d:b,c,f;e:b,g;f:b;g:c,f;;")
result = graph.search_szhk()
dot = create_print_render_dot(graph)

graph_strct = DiGraph(title="Exercise 05 Task 19 Graph 01",
                      filename="e05_t19_g01_structure",
                      allow_multi=True)
graph_strct.read_input(value="A:;C:A,A,A;D:A,C;")
dot_strct = create_print_render_dot(graph_strct)

print(result)

print("Found sZhk in graph e05_t19_g01:")
print("Depth-Number:\t{}".format(result.depth))
print("Min-Number:\t{}".format(result.min))
print("Root:\t\t{}".format(result.root))
print("sZhK:\t\t{}".format(result.szhk))

print_output_info(e="05", t="19")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print("\nEnd: Exercise 05 Task 19\n")
