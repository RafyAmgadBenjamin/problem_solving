def cal_min_dis(road_map, road_length):
    min_dist = 99999999999
    count = 0
    prev_letter = ""
    for i in range(road_length):
        if "Z" in road_map[i]:
            return 0
        if road_map[i] == "." and prev_letter != "":
            count += 1

        if road_map[i] == "R" or road_map[i] == "D":
            # This is the first time
            if prev_letter == "":
                prev_letter = road_map[i]
            elif prev_letter == road_map[i]:
                # in case R ... R or D ... D
                count = 0
            else:
                if min_dist > count + 1:
                    min_dist = count + 1
                prev_letter = road_map[i]
                count = 0
    return min_dist


while True:
    l = int(input())
    if l == 0:
        break
    road_map = input()
    min_dis = cal_min_dis(road_map, l)
    print(min_dis)

