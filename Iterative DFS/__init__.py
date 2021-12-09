import Utils


class State:
    liste = list()
    profond: int

    def __init__(self, liste, profond):
        self.liste = liste
        self.profond = profond


class DFSIterative:
    init_state = [1, 2, 0, 3, 4, 5, 6, 7, 8]
    final_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def parcours(self):
        game = Utils.Game()
        open = list()
        profond = 0
        state = State(self.init_state, profond)
        open.append(state)
        closed = {}
        limit = 0
        noeuds_dev = 0
        noeuds_vis = 0

        while Utils.list_to_string(self.final_state) not in closed :
            limit = limit + 1
            open = list()
            open.append(state)
            closed = {}
            profond = 0
            while len(open) != 0 and Utils.list_to_string(self.final_state) not in closed:
                if profond < limit:
                    noeuds_vis=noeuds_vis+len(closed)
                    noeuds_dev = noeuds_dev + len(open)+len(closed)
                    profond = profond + 1
                    s = open.pop(0)
                    l = s.liste
                    closed[Utils.list_to_string(l)] = profond
                    priorite = 0

                    if Utils.list_to_string(game.up(l)) not in closed:
                        open.insert(priorite, State(game.up(l), profond))
                        if profond == limit:
                            s = open.pop(priorite)
                            priorite = priorite - 1
                            l1 = s.liste
                            closed[Utils.list_to_string(l1)] = profond
                        priorite = priorite + 1

                    if Utils.list_to_string(game.down(l)) not in closed:
                        open.insert(priorite, State(game.down(l), profond))
                        if profond == limit:
                            s = open.pop(priorite)
                            priorite = priorite - 1
                            l1 = s.liste
                            closed[Utils.list_to_string(l1)] = profond
                        priorite = priorite + 1

                    if Utils.list_to_string(game.right(l)) not in closed:
                        open.insert(priorite, State(game.right(l), profond))
                        if profond == limit:
                            s = open.pop(priorite)
                            priorite = priorite - 1
                            l1 = s.liste
                            closed[Utils.list_to_string(l1)] = profond
                        priorite = priorite + 1
                    if Utils.list_to_string(game.left(l)) not in closed:
                        open.insert(priorite, State(game.left(l), profond))
                        if profond == limit:
                            s = open.pop(priorite)
                            l1 = s.liste
                            closed[Utils.list_to_string(l1)] = profond
                else:
                    profond = open[0].profond
        print('closed: ', closed.keys())
        print("profondeur = ", limit)
        print("nombre de noeuds stockés: ", noeuds_dev)
        print("nombre de noeuds visités: ", noeuds_vis)


def main():
    dfsI = DFSIterative()
    dfsI.parcours()


if __name__ == '__main__':
    main()
