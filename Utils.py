class Game:

    def up(self, liste):
        liste1=list(liste)
        pos = liste.index(0)
        if pos < 6:
            temp = liste[pos+3]
            liste1[pos] = temp
            liste1[pos+3] = 0
        return liste1

    def down(self, liste):
        liste1=list(liste)

        pos = liste.index(0)
        if pos > 2:
            temp = liste[pos - 3]
            liste1[pos] = temp
            liste1[pos - 3] = 0
        return liste1

    def right(self, liste):
        liste1=list(liste)

        pos = liste.index(0)
        if pos % 3 != 0:
            temp = liste[pos - 1]
            liste1[pos] = temp
            liste1[pos - 1] = 0
        return liste1

    def left(self, liste):
        liste1=list(liste)

        pos = liste.index(0)
        if pos % 3 != 2:
            temp = liste[pos + 1]
            liste1[pos] = temp
            liste1[pos + 1] = 0
        return liste1


def list_to_string(list):
    str1 = ""
    for ele in list:
        str1 += str(ele)
    return str1
