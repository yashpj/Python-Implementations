'''
You are in charge of overseeing the blueprint approval process for various architectural designs. Each blueprint has a specific complexity level, represented by an integer. Due to the complex nature of the designs, the approval process follows a strict order:

Blueprints with lower complexity should be reviewed first.
If a blueprint with higher complexity is submitted, it must wait until all simpler blueprints have been approved.
Your task is to simulate the blueprint approval process using a queue. You will receive a list of blueprints, each represented by their complexity level in the order they are submitted. 
Process the blueprints such that the simpler designs (lower numbers) are approved before more complex ones.

Return the order in which the blueprints are approved.



Understand: list of complexities , we need to stimulate the process using a queue.

[3,5,2,1,4]

dummy/stack = [5,3,3]
result = [3]
[3,5] -> [3] -> [] -> [2] ->[2,3,5]
[2,3,5] -> [] -> [1]

'''


def blueprint_approval(blueprints):
    dummy_stack = []
    result = []

    for i in blueprints:
        if len(result) == 0:
            result.append(i)
        else:
            while result and result[-1]>i:
                dummy_stack.append(result.pop())
            result.append(i)
            while dummy_stack:
                result.append(dummy_stack.pop())
    return result
    


print(blueprint_approval([3, 5, 2, 1, 4])) 
print(blueprint_approval([7, 4, 6, 2, 5])) 
