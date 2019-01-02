function dijkstra (graph, source) {
 
    const dist = [];
    const visited = [];
    const length = graph.length;

    function minimumDistance(dist, visited){
        let min = Infinity;
        let minIndex = -1;

        for(let i = 0; i < length; i++) {
            if(!visited[i] && dist[i] < min) {
                min = dist[i];
                minIndex = i;
            }
        }

        return minIndex;
    }

    for(let i = 0; i < length; i++){
        dist[i] = Infinity;
        visited[i] = false;
    }

    dist[source] = 0;

    for(let i = 0; i < length - 1; i++){
        const c = minimumDistance(dist, visited);
        visited[c] = true;

        for(let v = 0; v < length; v++){
            if(!visited[v] && graph[c][v] !== 0 && graph[c][v] + dist[c] < dist[v]){
                dist[v] = graph[c][v] + dist[c]
            }
        }
    }

    return dist;

}

const graph = 

 [[0,1,4,0,0],
  [0,0,2,0,1],
  [0,0,0,3,0],
  [0,0,0,0,0],
  [0,0,0,1,0]];

const graph2 = 

  [[0,2,4,0],
   [0,0,1,0],
   [0,0,0,1],
   [0,0,0,0]];

const graph3 = 

   [[0, 2, 4, 0, 0, 0],
    [0, 0, 1, 4, 2, 0],
    [0, 0, 0, 0, 3, 0],
    [0, 0, 0, 0, 0, 2],
    [0, 0, 0, 3, 0, 2],
    [0, 0, 0, 0, 0, 0]];



console.log(dijkstra(graph, 0))
console.log(dijkstra(graph2, 0))
console.log(dijkstra(graph3, 0))
// console.log(graph[0][0]);