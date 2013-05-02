__author__ = 'arobres'



class Commons(object):

    def to_dic(self, a_list):

        dic={}
        for item in a_list:
            if type(a_list) is list:
                dic.update(item)
            if type(a_list) is dict:
                dic=dict(dic.items()+a_list.items())
        return dic