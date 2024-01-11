class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)
        ticket_dict = collections.defaultdict(list)
        answer = []
        
        for src, dest in tickets:
            ticket_dict[src].append(dest)
        
        def dfs(current:str) -> None:
            while ticket_dict[current]:
                dfs(ticket_dict[current].pop())
            answer.append(current)
        
        dfs('JFK')
        return answer[::-1]