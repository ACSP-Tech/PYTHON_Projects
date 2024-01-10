import numpy as np

def calculate(values):
    matrix = np.array(values).reshape(3, 3)        
    result = {
       'mean':[matrix.mean(axis=0).tolist(), 
        matrix.mean(axis=1).tolist(), matrix.mean().tolist()],
       'variance':[matrix.var(axis=0).tolist(), 
        matrix.var(axis=1).tolist(), matrix.var().tolist()],
       'standard_deviation':[matrix.std(axis=0).tolist(), 
        matrix.std(axis=1).tolist(), matrix.std().tolist()],
       'max':[matrix.max(axis=0).tolist(), 
        matrix.max(axis=1).tolist(), matrix.max().tolist()],
       'min':[matrix.min(axis=0).tolist(), 
        matrix.min(axis=1).tolist(), matrix.min().tolist()],
       'sum':[matrix.sum(axis=0).tolist(), 
        matrix.sum(axis=1).tolist(), matrix.sum().tolist()]
    }
    return result


while True :
    try:
        values = input("Kindly input 9 integers: ").split()
        if len(values) != 9:
            error = input("try again! List must contain 9 integers separated by spaces: ").split()
            values = [int(val) for val in error]  
        if len(values) == 9:
            values = [int(val) for val in values]
            break
    except ValueError as e:
        print(f"Error: {e}")      
        continue
input_values = [int(val) for val in values]
result = calculate(input_values)
print(result)