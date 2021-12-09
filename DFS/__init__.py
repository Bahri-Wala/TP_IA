import Utils

class DFS:
    init_state = [1, 2, 0, 3, 4, 5, 6, 7, 8]
    final_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def parcours(self):
        game = Utils.Game()
        open = list()
        open.append(self.init_state)
        closed = {}
        while len(open) != 0 and Utils.list_to_string(self.final_state) not in closed:
            l=open.pop(0)
            closed[Utils.list_to_string(l)] = '1'
            priorite=0
            if Utils.list_to_string(game.up(l)) not in closed:
                open.insert(priorite, game.up(l))
                priorite=priorite+1
            if Utils.list_to_string(game.down(l)) not in closed:
                open.insert(priorite, game.down(l))
                priorite=priorite+1
            if Utils.list_to_string(game.right(l)) not in closed:
                open.insert(priorite, game.right(l))
                priorite=priorite+1
                priorite=priorite+1
            if Utils.list_to_string(game.left(l)) not in closed:
                open.insert(priorite,game.left(l))
        print(closed.keys())
        print("nombre de noeuds stockés: ", len(closed) + len(open))
        print("nombre de noeuds visités: ", len(closed))

def main():

    dfs = DFS()
    dfs.parcours()

if __name__ == '__main__':
    main()