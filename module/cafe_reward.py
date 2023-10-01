import time

from core.utils import pd_rgb, get_x_y
from gui.util import log


def implement(self):
    self.click(640, 521)
    time.sleep(2)
    self.click(274, 161)
    while self.pd_pos() != "cafe":
        self.click(274, 161)

    img_shot = self.get_screen_shot_array()
    path = "src/cafe/invitation_ticket.png"
    return_data1 = get_x_y(img_shot, path)
    print(return_data1)
    target_name = "响"
    if return_data1[1][0] <= 1e-03:
        log.d("invitation available begin find student " + target_name, 1, logger_box=self.loggerBox)
        self.click(return_data1[0][0], return_data1[0][1])
        time.sleep(1)
        x_location = 790
        y_location = [218, 317, 395, 468, 550, 596]
        swipe_x = 630
        swipe_y = 580
        dy = 430

        student_name = ["爱丽丝", "切里诺", "志美子", "日富美", "佳代子", "明日奈", "菲娜", "艾米", "真纪",
                        "泉奈", "明里", "芹香", "优香",
                        "花江", "纯子", "千世", "干世", "莲见", "爱理", "睦月", "野宫", "绫音", "歌原",
                        "芹娜", "小玉", "铃美", "朱莉", "好美", "千夏", "琴里",
                        "春香", "真白", "鹤城", "爱露", "晴奈", "日奈", "伊织", "星野",
                        "白子", "柚子", "花凛", "妮露", "纱绫", "静子", "花子", "风香",
                        "和香", "和香", "茜", "泉", "梓", "绿", "堇", "瞬", "桃", "椿", "晴", "响"]
        stop_flag = False
        last_student_name = None
        while not stop_flag:
            img_shot = self.get_screen_shot_array()
            name_st = self.img_ocr(img_shot)
            detected_name = []
            i = 0
            while i < len(name_st):
                for j in range(0, len(student_name)):
                    if name_st[i] == student_name[j][0]:
                        flag = True
                        for k in range(1, len(student_name[j])):
                            if name_st[i + k] != student_name[j][k]:
                                flag = False
                                break
                        if flag:
                            if student_name[j] == "干世":
                                detected_name.append("千世")
                            else:
                                detected_name.append(student_name[j])
                            i = i + len(student_name[j]) - 1
                            break
                i = i + 1
            st = ""
            for s in range(0, len(detected_name)):
                st = st + str(detected_name[s]) + " "
            if st == "":
                log.d("No name detected", 2, logger_box=self.loggerBox)
                stop_flag = True
            log.d("detected name :" + st, 1, logger_box=self.loggerBox)
            if detected_name[len(detected_name) - 1] == last_student_name:
                log.d("Can't detect target student", 2, logger_box=self.loggerBox)
                self.click(271, 281)
                time.sleep(0.2)
                stop_flag = True
            else:
                last_student_name = detected_name[len(detected_name) - 1]
                for s in range(0, len(detected_name)):
                    if detected_name[s] == target_name:
                        log.d("find student", level=1, logger_box=self.loggerBox)
                        stop_flag = True
                        self.click(x_location, y_location[s])
                        time.sleep(0.5)
                        self.click(770, 500)
                        time.sleep(2)
                        self.click(274, 161)
                        while self.pd_pos() != "cafe":
                            self.click(274, 161)
                        break
                if not stop_flag:
                    self.connection.swipe(swipe_x, swipe_y, swipe_x, swipe_y - dy, 1)
                    self.click(617, 500)
    else:
        log.d("invitation ticket used", 2, logger_box=self.loggerBox)
    start_x = 640
    start_y = 360
    swipe_action_list = [[640, 640, 0, -640, -640, -640, -640, 0, 640, 640, 640],
                         [0, 0, -360, 0, 0, 0, 0, -360, 0, 0, 0]]
    for i in range(0, len(swipe_action_list[0])):
        while self.pd_pos(anywhere=True) != "cafe":
            self.click(640, 360)
        stop_flag = False
        while not stop_flag:
            shot = self.get_screen_shot_array()
            location = []
            #  print(shot.shape)
            #  for i in range(0, 720):
            #      print(shot[i][664][:])
            for x in range(0, 1280):
                for y in range(0, 670):
                    if pd_rgb(shot, x, y, 255, 255, 210, 230, 0, 30) and \
                            pd_rgb(shot, x, y + 21, 255, 255, 210, 230, 0, 30) and \
                            pd_rgb(shot, x, y + 41, 255, 255, 210, 230, 0, 30):
                        location.append([x, y + 42])
                        for tmp1 in range(-40, 40):
                            for tmp2 in range(-40, 40):
                                if 0 <= x + tmp1 < 1280:
                                    shot[y + tmp2][x + tmp1] = [0, 0, 0]
                                else:
                                    break

            if len(location) == 0:
                log.d("no interaction swipe to next stage", 1, logger_box=self.loggerBox)
                stop_flag = True
            else:
                log.d("find " + str(len(location)) + " interaction available", 1, logger_box=self.loggerBox)
                for tt in range(0, len(location)):
                    self.click(location[tt][0], location[tt][1])
                    time.sleep(0.1)

        self.connection.swipe(start_x, start_y, start_x + swipe_action_list[0][i],
                              start_y + swipe_action_list[1][i], 0.1)
    log.d("cafe task finished", 1, logger_box=self.loggerBox)
    self.main_activity[0][1] = 1
