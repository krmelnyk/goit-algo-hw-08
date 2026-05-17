import heapq


def min_connection_cost(cables):
    if len(cables) <= 1:
        return 0

    heap = cables.copy()
    heapq.heapify(heap)

    total_cost = 0

    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        connection_cost = first + second

        total_cost += connection_cost
        heapq.heappush(heap, connection_cost)

    return total_cost


if __name__ == "__main__":
    cables = [4, 3, 2, 6]

    print(f"Cables: {cables}")
    print(f"Minimum total connection cost: {min_connection_cost(cables)}")
