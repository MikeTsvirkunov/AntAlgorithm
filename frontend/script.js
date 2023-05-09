var graph = {
    nodes: [
        { "id": "n0", "label": "A (0, 0)", x: 0, y: 0, size: 3, color: '#008cc2' },
        { "id": "n1", "label": "A (3, 1)", x: 3, y: 1, size: 2, color: '#008cc2' },
        { "id": "n2", "label": "A (1, 3)", x: 1, y: 3, size: 1, color: '#E57821' }
    ],
    edges: [
        { "id": "e0", "source": "n0", "target": "n1", color: '#282c34', type:'line', size:0.5 },
        { "id": "e1", "source": "n1", "target": "n2", color: '#282c34', type:'curve', size:1},
        { "id": "e2", "source": "n2", "target": "n0", color: '#FF0000', type:'line', size:2}
    ]
    }

// Инициализируем библиотеку Sigma.js
var s = new sigma({
    container: 'graph-container',
    graph: graph,
    renderer: {
        container: document.getElementById('graph-container'),
        type: 'canvas'
    },
    settings: {
        nodeLabelColor: 'node',
        defaultEdgeLabelColor: '#ccc',
        edgeLabelThreshold: 3,
        zoomMin: 0.1,
        zoomMax: 10
    }
});

// // create a graph class
// class Graph {
//     // defining vertex array and
//     // adjacent list
//     constructor(noOfVertices)
//     {
//         this.noOfVertices = noOfVertices;
//         this.AdjList = new Map();
//     }
 
//     // functions to be implemented
 
//     // add vertex to the graph
//     addVertex(v)
//         {
//             // initialize the adjacent list with a
//             // null array
//             this.AdjList.set(v, []);
//         }
//     // add edge to the graph
//     addEdge(v, w)
//         {
//             // get the list for vertex v and put the
//             // vertex w denoting edge between v and w
//             this.AdjList.get(v).push(w);
        
//             // Since graph is undirected,
//             // add an edge from w to v also
//             this.AdjList.get(w).push(v);
//         }
//     // Prints the vertex and adjacency list
//     printGraph()
//     {
//         // get all the vertices
//         var get_keys = this.AdjList.keys();
    
//         // iterate over the vertices
//         for (var i of get_keys)
//             {
//                 // get the corresponding adjacency list
//                 // for the vertex
//                 var get_values = this.AdjList.get(i);
//                 var conc = "";
        
//                 // iterate over the adjacency list
//                 // concatenate the values into a string
//                 for (var j of get_values)
//                     conc += j + " ";
        
//                 // print the vertex and its adjacency list
//                 console.log(i + " -> " + conc);
//             }
//     }
 
//     // bfs(v)
//     // dfs(v)
// }


// var g = new Graph(6);
// var vertices = [ 'A', 'B', 'C', 'D', 'E', 'F' ];
 
// // adding vertices
// for (var i = 0; i < vertices.length; i++) {
//     g.addVertex(vertices[i]);
// }
 
// // adding edges
// g.addEdge('A', 'B');
// g.addEdge('A', 'D');
// g.addEdge('A', 'E');
// g.addEdge('B', 'C');
// g.addEdge('D', 'E');
// g.addEdge('E', 'F');
// g.addEdge('E', 'C');
// g.addEdge('C', 'F');
 
// // prints all vertex and
// // its adjacency list
// // A -> B D E
// // B -> A C
// // C -> B E F
// // D -> A E
// // E -> A D F C
// // F -> E C
// g.printGraph();

