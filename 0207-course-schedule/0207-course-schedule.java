class Solution {
    List<List<Integer> > graph;
    boolean[] visited;
    
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        graph = new ArrayList<>();
        visited = new boolean[numCourses];
        
        for (int i = 0; i < numCourses; i++) {
            graph.add(new ArrayList<>());
        }
        
        for (int[] courses : prerequisites) {
            graph.get(courses[1]).add(courses[0]);
        }
        
        for (int i = 0; i < numCourses; i++) {
            if(!visited[i] && hasCycle(i, new HashSet<Integer>())) {
                return false;
            }
        }
        
        return true;
    }
    
    public boolean hasCycle(int node, Set<Integer> tracker) {
        tracker.add(node);
        visited[node] = true;
        
        for (Integer next : graph.get(node)) {
            if (!visited[next] && hasCycle(next, tracker)) {
                return true;
            } else if(tracker.contains(next)) {
                return true;
            }            
        }
        tracker.remove(node);
        
        return false;
    }
}