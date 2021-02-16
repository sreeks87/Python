import requests
class Draw:
    def call_api(year):
        t=0
        for i in range(1,20):
            url="https://jsonmock.hackerrank.com/api/football_matches?year="+year+"&team1goals="+str(i)+"&team2goals="+str(i)+"&page=1"
            print(url)
            r=requests.get(url)
            t+=r.json()['total']

        return t


print(Draw.call_api(input("Year: ")))




