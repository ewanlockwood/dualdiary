{"filter":false,"title":"utils.py","tooltip":"/cal/utils.py","ace":{"folds":[],"scrolltop":362.5,"scrollleft":0,"selection":{"start":{"row":39,"column":12},"end":{"row":39,"column":12},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"hash":"80229887bd2158621a8c9cbd8bf43733c0019fb4","undoManager":{"mark":2,"position":2,"stack":[[{"start":{"row":31,"column":82},"end":{"row":31,"column":83},"action":"remove","lines":["}"],"id":2}],[{"start":{"row":31,"column":17},"end":{"row":31,"column":18},"action":"remove","lines":["{"],"id":3}],[{"start":{"row":4,"column":0},"end":{"row":38,"column":4},"action":"remove","lines":["class Calendar(HTMLCalendar):","    def __init__(self, year=None, month=None):","        self.year = year","        self.month = month","        super(Calendar, self).__init__()","        ","    def formatday(self, day, events):","        events_per_day = events.filter(start_time_day=day)","        d = ''","        ","        for event in events_per_day:","            d+= f'<li> {{event.title}} </li>'","            ","        if day != 0:","            return f\"<td><span class='date'> {{day}} </span><ul> {{d}} </ul></td>\"","        return '<td></td>'","        ","    def formatweek(self, theweek, events):","        week = ''","        for d, weekday in theweek:","            week+= self.formatday(d, events)","        return f'<tr> {{week}} </tr>'","        ","    def formatmonth(self, withyear=True):","        events = Event.objects.filter(start_time_year=self.year, start_time_month=self.month)","        ","        cal = f'<table border=\"0\" cellpadding=\"0\" cellspacing=\"0\" class=\"calendar\">\\n'","        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\\n'","        cal += f'{self.formatweekheader()}\\n'","        ","        for week in self.monthdays2calendar(self.year, self.month):","            cal += f'{{self.formatweek(week, events)}}\\n'","        return cal","        ","    "]},{"start":{"row":4,"column":0},"end":{"row":39,"column":12},"action":"insert","lines":["class Calendar(HTMLCalendar):","\tdef __init__(self, year=None, month=None):","\t\tself.year = year","\t\tself.month = month","\t\tsuper(Calendar, self).__init__()","","\t# formats a day as a td","\t# filter events by day","\tdef formatday(self, day, events):","\t\tevents_per_day = events.filter(start_time__day=day)","\t\td = ''","\t\tfor event in events_per_day:","\t\t\td += f'<li> {event.title} </li>'","","\t\tif day != 0:","\t\t\treturn f\"<td><span class='date'>{day}</span><ul> {d} </ul></td>\"","\t\treturn '<td></td>'","","\t# formats a week as a tr ","\tdef formatweek(self, theweek, events):","\t\tweek = ''","\t\tfor d, weekday in theweek:","\t\t\tweek += self.formatday(d, events)","\t\treturn f'<tr> {week} </tr>'","","\t# formats a month as a table","\t# filter events by year and month","\tdef formatmonth(self, withyear=True):","\t\tevents = Event.objects.filter(start_time__year=self.year, start_time__month=self.month)","","\t\tcal = f'<table border=\"0\" cellpadding=\"0\" cellspacing=\"0\" class=\"calendar\">\\n'","\t\tcal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\\n'","\t\tcal += f'{self.formatweekheader()}\\n'","\t\tfor week in self.monthdays2calendar(self.year, self.month):","\t\t\tcal += f'{self.formatweek(week, events)}\\n'","\t\treturn cal"]}]]},"timestamp":1572263333207}