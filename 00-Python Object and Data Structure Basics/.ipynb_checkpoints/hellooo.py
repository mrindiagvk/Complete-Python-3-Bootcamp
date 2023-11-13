
class varun:
    def __init__(self):
        self.items={}
    def varuns_wish(self,devices,names):
        self.items[devices]=names
    def get_varuns_wish(self):
        print(self.items)
    def remove_varuns_wish(self,item):
        del self.items[item]

varunss_wishes=varun()
varunss_wishes.varuns_wish("apple","macbookpro")
varunss_wishes.varuns_wish("android","nothoing2")
varunss_wishes.varuns_wish("watch","apple")
varunss_wishes.get_varuns_wish()
varunss_wishes.remove_varuns_wish("android")
varunss_wishes.get_varuns_wish()