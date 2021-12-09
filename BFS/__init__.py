import Utils

class BFS:
    init_state = [1, 2, 0, 3, 4, 5, 6, 7, 8]
    final_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def parcours(self):
        game = Utils.Game()
        open = list()
        open.append(self.init_state)
        closed = {}
        while len(open) != 0 and Utils.list_to_string(self.final_state) not in closed:
            temp = list(open)
            open = list()
            for l in temp:
                closed[Utils.list_to_string(l)]='1'
                if Utils.list_to_string(game.up(l)) not in closed:
                    open.append(game.up(l))
                if Utils.list_to_string(game.down(l)) not in closed:
                    open.append(game.down(l))
                if Utils.list_to_string(game.right(l)) not in closed:
                    open.append(game.right(l))
                if Utils.list_to_string(game.left(l)) not in closed:
                    open.append(game.left(l))
        print(closed.keys())
        print("nombre de noeuds stockés: ", len(closed) + len(open))
        print("nombre de noeuds visités: ", len(closed))


def main():

    bfs = BFS()
    bfs.parcours()

if __name__ == '__main__':
    main()

