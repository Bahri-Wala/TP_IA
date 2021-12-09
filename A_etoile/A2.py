import Utils


class State:
    liste = list()
    f: int
    profond: int

    def __init__(self, liste, f,profond):
        self.liste = liste
        self.f = f
        self.profond = profond

def heuristique1(liste):
    deplacements = 0
    for i in range(0,9):
        if liste[i] != i and liste[i] != 0:
            deplacements = deplacements + abs(i%3-liste[i]%3) + abs(int(i/3)-int(liste[i]/3))
    return deplacements

class A1:
    init_state = [1, 2, 3, 4, 5, 0, 6, 7, 8]
    final_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def parcours(self):
        game = Utils.Game()
        open = list()
        profond = 0
        state = State(self.init_state, heuristique1(self.init_state), profond)
        open.append(state)
        closed = {}
        i = 0
        while len(open) != 0 and Utils.list_to_string(self.final_state) not in closed:
            i = i + 1

            open.sort(key=lambda elem: elem.f)
            profond = open[0].profond
            profond = profond + 1
            s = open.pop(0)
            l = s.liste
            f = heuristique1(l) + profond
            closed[Utils.list_to_string(l)] = f

            if Utils.list_to_string(game.up(l)) not in closed:
                open.insert(0, State(game.up(l), profond + heuristique1(game.up(l)), profond))

            if Utils.list_to_string(game.down(l)) not in closed:
                open.insert(0, State(game.down(l), profond + heuristique1(game.down(l)), profond))

            if Utils.list_to_string(game.right(l)) not in closed:
                open.insert(0, State(game.right(l), profond + heuristique1(game.right(l)), profond))

            if Utils.list_to_string(game.left(l)) not in closed:
                open.insert(0, State(game.left(l), profond + heuristique1(game.left(l)), profond))

        print('closed: ', closed.keys())
        print("nombre de noeuds stockés: ", len(open)+len(closed))
        print("nombre de noeuds visités: ", len(closed))


def main():

    a1 = A1()
    a1.parcours()


if __name__ == '__main__':
    main()