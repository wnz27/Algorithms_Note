'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-14 11:01:42
@LastEditTime: 2020-03-14 15:28:18
@FilePath: /Algorithms_Note/其他面试题目/self——高频面试题频率粗略计算.py
@description: type some description
'''
import collections
def countFrequence(arr):
    """
    type:list[题号]
    rtype:dict{题号：频率}
    description:并按照频率从高到低排序
    """
    helper = {}
    count = 0
    for title in arr:
        key = "题目:[# " + str(title) + "]"
        helper[key] = helper.setdefault(key, 0) + 1
        count += 1
    helper["题目总数为:"] = count
    # 按题目频率值由大到小排序
    order_dict = collections.OrderedDict(sorted(helper.items(), key=lambda x: x[1], reverse=True))
    return order_dict

a = countFrequence([1,2,3,4,5,2,3,8,1,1,1,3,3,4,5])
print(a)
print(a["题目:[# 2]"])

problem_title = [771, 672, 186, 721, 360, 493, 321, 446, 986, 808, 975, 636, 855, 
420, 900, 42, 733, 835, 359, 384,212, 157, 706, 796, 339, 488, 1044, 364, 793, 457, 
412, 635, 463, 332, 1192, 1197, 308, 382, 314, 68, 227, 864, 906, 149, 296, 1031, 1, 
734, 1040, 253, 692, 329, 282, 675, 708, 497, 238, 973, 616, 54, 1181, 782, 1140, 
419, 369, 489, 295, 140, 380, 317, 291, 943, 514, 527, 271, 273, 729, 97, 458, 609, 
632, 388, 418, 895, 1279, 772, 427, 277, 909, 411, 472, 466, 688, 465, 741, 996, 642,
351, 1278, 336, 431, 981, 333, 737, 218, 305, 146, 261, 591, 528, 356, 249, 381, 
805, 711, 460, 911, 736, 353, 393, 694, 391, 352, 1060, 251, 770, 341, 281, 311, 
403, 1095, 284, 428, 479, 269, 348, 588, 549, 545, 362, 43, 537, 121, 133, 827, 22, 
384, 1, 72, 829, 2, 3, 15, 91, 179, 25, 104, 120, 283, 192, 9, 21, 350, 53, 20, 70, 
76, 528, 997, 18, 312, 15, 3, 53, 5, 70, 226, 440, 478, 4, 72, 7, 2, 178, 198, 206, 
347, 386, 674, 709, 200, 221, 295, 294, 541, 58, 155, 54, 20, 333, 518, 402, 136, 
398, 1, 232, 9, 91, 803, 736, 815, 679, 850, 782, 403, 741, 1106, 820, 631, 1163, 
499, 1109, 423, 385, 593, 1151, 85, 1245, 600, 362, 394, 843, 799, 254, 355, 582, 
562, 1031, 45, 554, 316, 221, 881, 5, 539, 639, 1044, 43, 758, 323, 1162, 491, 224, 
227, 32, 72, 192, 997, 987, 778, 16.26, 870, 801, 93, 583, 1262, 515, 1165, 37, 325, 
289, 735, 638, 163, 1160, 1267, 3, 419, 200, 135, 992, 354, 186, 791, 406, 1027, 301, 
442, 462, 08.07, 187, 739, 273, 233, 695, 841, 535, 678, 1124, 329, 836, 1171, 652, 
315, 415, 1019, 470, 344, 348, 273, 277, 642, 428, 545, 722, 285, 1369, 186, 253, 
138, 218, 419, 772, 591, 564, 362, 269, 636, 972, 1279, 489, 158, 431, 588, 708, 
510, 535, 1273, 151, 314, 694, 794, 449, 836, 379, 460, 909, 935, 727, 805, 702, 
346, 457, 402, 528, 358, 688, 146, 353, 252, 403, 568, 297, 333, 450, 490, 212, 
340, 651, 1198, 224, 631, 1092, 223, 317, 445, 1285, 1197, 165, 311, 729, 308, 
1187, 356, 716, 426, 759, 432, 161, 116, 280, 706, 679, 443, 140, 1246, 384, 885, 
1093, 863, 54, 407, 281, 270, 173, 672, 271, 117, 351, 168, 295, 103, 768, 529, 229, 
833, 266, 286, 458, 42, 73, 68, 380, 200, 267, 1192, 465, 44, 558, 126, 958, 843, 
149, 683, 430, 632, 1067, 1239, 174, 471, 248, 981, 1206, 493, 505, 468, 227, 261]
result = countFrequence(problem_title)
print(result)