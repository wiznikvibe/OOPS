# q10 :Try to find out a number of occurances of all the data 
# q11 : Try to find out number of keys in dict element
# q12 : Try to filter out all the string data 
# q13 : Try to Find  out alphanum in data
# q14 : Try to find out multiplication of all numeric value in  the individual collection inside dataset 
# q15 : Try to unwrape all the collection inside collection and create a flat list 
import logging
logging.basicConfig(filename="logs/test.log", level=logging.INFO, format='%(levelname)s %(asctime)s %(name)s: %(message)s')
# logging.info("This is my second code for logging.")
# logging.warning("this is will generate a warning message in the log file.")
class Tasks:
    # def __init__(self, num_list):
    def extract_entities(self,data: list, entity_type: type):
        try:
            entities = [i for i in data if isinstance(i, entity_type)]
            logging.info(f"These are all the {entity_type.__name__} entities in the data given: ")
            for entity in entities:
                logging.info(entity)
            return entities
        except Exception as e:
            logging.exception(e)

    def extract_numericals(self, data: list):
        try:
            numerical_values = []
            if isinstance(data, (int, float)):
                numerical_values.append(data)
            elif isinstance(data, (list, tuple, set)):
                for item in data:
                    numerical_values.extend(self.extract_numericals(item))
            elif isinstance(data, dict):
                for key, value in data.items():
                    numerical_values.extend(self.extract_numericals(value))
                    numerical_values.extend(self.extract_numericals(key))
            return numerical_values
        except Exception as e:
            logging.exception(e)
    
    def summation(self, data):
        try:
            res_list = self.extract_numericals(data)
            logging.info(f"This is the list of Numericals {res_list}")
            total = 0
            for i in res_list:
                total += i
            return total
        except Exception as e:
            logging.exception(e)
    
    def odd_numbers(self):
        try:
            data = self.extract_numericals(list_entities)
            logging.info(f"These are list {data}")
            odd_num = []
            for i in data:
                
                if type(i) == int and i % 2 == 1:
                    odd_num.append(i)
            return odd_num
        except Exception as e:
            logging.exception(e)

    def text_search(self, data, text):
        try:
            if isinstance(data,dict):
                logging.info(f"This is the Dictionary Variable where {text} was found")
                for value in data.keys():
                    if isinstance(value, str) and value == text:
                        return value 
            elif isinstance(data, (list,set,tuple)):
                logging.info(f"This is a container where the {text} was found.")
                for item in data:
                    if isinstance(item, str) and item == text:
                        return item
                    elif isinstance(item, dict):
                        logging.info("This is a dicitionary inside a list")
                        result = self.text_search(item,text)
                        if result is not None:
                            return result
            return None
        except Exception as e:
            logging.exception(e)    




l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]

var_func = Tasks()

list_entities = var_func.extract_entities(l, list)
dict_entities = var_func.extract_entities(l, dict)
tuple_entities = var_func.extract_entities(l, tuple)
set_entities = var_func.extract_entities(l, set)
num_res = var_func.extract_numericals(l)
total = var_func.summation(l)
odd_entities = var_func.odd_numbers() 
text_doc = var_func.text_search(l, "ineuron") 
print(text_doc)
print(odd_entities)
print(total)
print(num_res)

print(list_entities)
print(dict_entities)
print(tuple_entities)
print(set_entities)



