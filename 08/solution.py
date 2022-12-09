file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()



def part_one():
    visible = []

    for i in range(1, len(myin[0])-1):
        vert = [int(l[i]) for l in myin]
        for j in range(1, len(vert)-1):
            if vert[j] > max(vert[:j]) or vert[j] > max(vert[j + 1:]):
                visible.append(str(i) + "," + str(j))

    for i in range(1, len(myin)-1):
        horiz = [int(x) for x in myin[i]]
        for j in range(1, len(horiz) - 1):
            if horiz[j] > max(horiz[:j]) or horiz[j] > max(horiz[j + 1:]):
                visible.append(str(j) + "," + str(i))

    print(len(set(visible)) + len(myin[0]) * 2 + (len(myin) - 2) * 2)

def get_vis(index, view_line):
    score = [0, 0]

    for i in range(index-1, -1, -1):
        if view_line[i]<view_line[index]:
            score[0] += 1
        else:
            score[0] += 1
            break

    for i in range(index+1, len(view_line)):
        if view_line[i]<view_line[index]:
            score[1] += 1
        else:
            score[1] += 1
            break

    return score[0] * score[1]

def part_two():
    scene_scores = []

    for i in range(len(myin)):
        for j in range(len(myin[0])):
            vert = [int(l[j]) for l in myin]
            horiz = [int(x) for x in myin[i]]
            scene_scores.append(get_vis(i, vert) * get_vis(j, horiz))

    print(max(scene_scores))


part_one()
part_two()