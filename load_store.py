           
class LS(object):
    def __init__(self, RESVNUMCONFIG):
        self.ls = {            
            'LOAD': [
                {
                    'time': "",
                    'busy': False,
                    "vk": "-",
                    "qk": "-",
                    "dest" : "-",
                    'Name': "Load" + str(t),
                    'insr_pc': ""
                }
                for t in range(RESVNUMCONFIG['LOAD'])],
            'STORE': [
                {
                    'time': -1,
                    'busy': False,
                    "vj": "-",
                    "vk": "-",
                    "qj": "-",
                    "qk": "-",
                    'addr': 0,
                    'Name': "Load" + str(t),
                    'insr_pc': ""
                }
                for t in range(RESVNUMCONFIG['STORE'])],
        }

        