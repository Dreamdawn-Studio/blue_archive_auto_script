from get_location import Location
import log


class Solver(Location):
    def __init__(self):
        super().__init__()
        self.main_activity = ["mail", "schedule", "energy_clear", "cafe", "momo_talk", "create",
                              "story", "combat_power_fight", "arena", "rewarded_task", "collect_daily_reward"]
        for i in range(0, len(self.main_activity)):
            self.main_activity[i] = [self.main_activity[i], 0]
            print(self.main_activity[i])

    def solve(self):
        for i in range(0, len(self.main_activity)):
            if self.main_activity[i][0] == "mail":
                pass
