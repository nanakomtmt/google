#!/usr/bin/env python3

import sys
import math

from common import print_tour, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def greedy_solve(cities):
    N = len(cities)

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(i, N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])
            
    current_city = 0
    unvisited_cities = set(range(1, N))
    tour = [current_city]
    # print(unvisited_cities)

    while unvisited_cities:
        next_city = min(unvisited_cities,
                        key=lambda city: dist[current_city][city])
        unvisited_cities.remove(next_city)
        tour.append(next_city)
        current_city = next_city
    return tour,dist


def swap_two_way(tour, dist):
    count=1
    while count>0:
        count = 0
        for i in range(len(tour)-2):
            for j in range(i+2, len(tour)):
                nextJ=j+1
                if j+1==len(tour):
                    nextJ=0
                AtoB = dist[tour[i]][tour[i + 1]]
                CtoD = dist[tour[j]][tour[nextJ]]
                AtoC = dist[tour[i]][tour[j]]
                BtoD = dist[tour[i + 1]][tour[nextJ]]
                if AtoB + CtoD > AtoC + BtoD:
                    swap = tour[i+1 : j+1]
                    tour[i+1 : j+1] = reversed(swap)
                    count += 1
        
    return tour



if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour,dist = greedy_solve(read_input(sys.argv[1]))
    tour=swap_two_way(tour,dist)
    print_tour(tour)
