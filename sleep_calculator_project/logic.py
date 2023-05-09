class sleep_logic:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes=minutes

    def time_calculation(hours, minutes):
        """returns times when you should go to bed"""
        t_in_min = 60*hours + minutes
        wake_up_times = []
        for i in range(1, 7):
            # 15 additional minutes to fall asleep
            if t_in_min-(i*90+15) < 0:
                t_in_min+= (24*60)
            wake_up_times.append(sleep_logic.convert_m_into_h_and_m(t_in_min-(i*90+15)))
        return wake_up_times

    def convert_m_into_h_and_m(minutes):
        """convenient way of dealing with time formats"""
        hours = minutes // 60
        minutes = minutes % 60
        formatted_time = [hours, minutes]
        return formatted_time





