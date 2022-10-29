# Inspired by
# https://tgmstat.wordpress.com/2013/06/12/draw-neural-network-diagrams-graphviz/
# https://github.com/martisak/dotnets
# @author rongrongstudio
# @date 10/30/2022
import os


class BPNeuralNetworkDrawing(object):
    """
    function:Drawing BP Neural Network Architecture
    @:parameter
        layers[list]:Number of neurons in each layer
        name[str]:Picture Name
        path[str]:Picture Path default:'bpimg'
    @:return
        None
    """

    def __init__(self, layers: list, name: str, path='bpimg'):
        self.layers = layers
        self.layers_string = ["Input"] + ["Hidden"] * (len(self.layers) - 2) + ["Output"]
        self.layers_color = ["none"] + ["none"] * (len(self.layers) - 2) + ["none"]
        self.layers_fillcolor = ["black"] + ["gray"] * (len(self.layers) - 2) + ["black"]
        self.penwidth = 10
        self.name = name
        self.path = path

    def drawing(self):
        if self.path not in os.listdir():
            os.mkdir(self.path)
        with open(self.path + '/' + self.name, 'w') as f:
            f.write("digraph G {\n")
            f.write("\trankdir=LR\n")
            f.write("\tsplines=line\n")
            f.write("\tnodesep=.08;\n")
            f.write("\tranksep=1;\n")
            f.write("\tedge [color=black, arrowsize=.5];\n")
            f.write("\tnode [fixedsize=true,label=\"\",style=filled," + "color=none,fillcolor=gray,shape=circle];\n")
            f.write("\n")

            # Clusters
            for i in range(len(self.layers)):
                f.write(f"\tsubgraph cluster_{i} {{\n")
                f.write(f"\t\tcolor={self.layers_color[i]};\n")
                f.write(
                    f"\t\tnode [style=filled, color=white, penwidth={self.penwidth},fillcolor={self.layers_fillcolor[i]} shape=circle];\n")
                f.write("\t\t")
                for a in range(self.layers[i]):
                    f.write(f"l{i + 1}{a}  ")
                f.write(";\n")
                f.write(f"\t\tlabel = {self.layers_string[i]};\n")
                f.write("\t}\n")
                f.write("\n")

            # Nodes
            for i in range(1, len(self.layers)):
                for a in range(self.layers[i - 1]):
                    for b in range(self.layers[i]):
                        f.write(f"\tl{i}{a} -> l{i + 1}{b}\n")

            f.write("}\n")

    def run(self):
        self.drawing()
        os.system(f'dot -Tpng -O {self.path}/{self.name}')


if __name__ == '__main__':
    bpdrawing = BPNeuralNetworkDrawing([3, 7, 7, 2], 'test')
    bpdrawing.run()
