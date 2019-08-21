#%%
import hashlib

#%%
class HashUtils(object):

    def __init__(self):

        pass

    def hash(self, string):
        """
            Generate hash from string

            Args: 
                - string
            Return:
                - hash
        """
        return hashlib.md5(string.encode('utf-8')).hexdigest()

    def hd(self, row_list):
        """
            Generate hash diff from list

            Args: 
                - row_list : list
            Return:
                - hash
        """
        string = ""
        for i in range(2, len(row_list)):
            string = string + str(row_list[i])

        return self.hash(string)

    def hk(self, row_list, index_list):
        """
            Generate hash key from list

            Args: 
                - row_list : list
                - index_list : index for row_list that to be hashed
            Return:
                - hash
        """
        string = ""
        for index in index_list:
            string = string + str(row_list[index])

        return self.hash(string)
        


#%%
