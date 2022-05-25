#! /usr/bin/python3

def read_number(line, index):
    number = 0
    while index < len(line) and line[index].isdigit():
        number = number * 10 + int(line[index])
        index += 1
    if index < len(line) and line[index] == '.':
        digit = 1  # 小数第何位なのかを保存する
        index += 1
        while index < len(line) and line[index].isdigit():
            number += int(line[index])*(0.1**digit)
            index += 1
            digit += 1
    token = {'type': 'NUMBER', 'number': number}
    return token, index


def read_plus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1


def read_minus(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1


def read_times(line, index):
    token = {'type': 'TIMES'}
    return token, index + 1


def read_divide(line, index):
    token = {'type': 'DIVIDE'}
    return token, index + 1

def read_brackets_left(line, index):
    token = {'type': 'BRACKETS_LEFT'}
    return token, index + 1

def read_brackets_right(line, index):
    token = {'type': 'BRACKETS_RIGHT'}
    return token, index + 1


def tokenize(line):
    """
    Tokenize the input line and return a list of tokens
    """
    tokens = []
    index = 0
    brackets_count=0
    while index < len(line):
        if line[index].isdigit():
            (token, index) = read_number(line, index)
        elif line[index] == '+':
            (token, index) = read_plus(line, index)
        elif line[index] == '-':
            (token, index) = read_minus(line, index)
        elif line[index] == '*':
            (token, index) = read_times(line, index)
        elif line[index] == '/':
            (token, index) = read_divide(line, index)
        elif line[index] == '(':
            brackets_count+=1
            (token, index)=read_brackets_left(line, index)
            
        elif line[index] == ')':
            
            (token, index)=read_brackets_right(line, index)
        else:
            print('Invalid character found: ' + line[index])
            exit(1)
        tokens.append(token)
    return tokens,brackets_count


def evaluate_times_divide(tokens):
    new_tokens = []
    index = 0
    while index < len(tokens):    
        if tokens[index]['type'] == 'TIMES':
            new_tokens[len(new_tokens) -
                       1]['number'] *= tokens[index+1]['number']
            index += 1
        elif tokens[index]['type'] == 'DIVIDE':
            new_tokens[len(new_tokens) -
                       1]['number'] /= tokens[index+1]['number']
            index += 1
        else:
            new_tokens.append(tokens[index])
        index += 1
    #     print(new_tokens)
    # print(new_tokens)
    return new_tokens


def evaluate_plus_minus(tokens):
    """
    Evaluate the list of tokens and return a calculated result
    """
    answer = 0
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'PLUS':
                answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
            else:
                print('Invalid syntax')
        index += 1

    return answer


def insert_dummy_plus(tokens):
    tokens.insert(0, {'type': 'PLUS'})
    return tokens

def calculate_smallest_bracket(tokens,left,right):
    part_tokens=[]
    for j in range(left[len(left)-1],right[0]):           
        part_tokens.append(tokens[j+1])
    
    answer = calculate_tokens(part_tokens)

    del tokens[left[len(left)-1]:right[0]+1]
    tokens.insert(left[len(left)-1], {'type': 'NUMBER', 'number': answer})
    return tokens
 

def find_smallest_bracket(tokens):
    brackets_left_index=[]
    brackets_right_index=[]
    for i in range(len(tokens)):
        if tokens[i]['type']=='BRACKETS_LEFT':
            brackets_left_index.append(i)
        elif tokens[i]['type']=='BRACKETS_RIGHT':
            brackets_right_index.append(i)
            break
    return brackets_left_index,brackets_right_index

def calculate_tokens(tokens):
    tokens = insert_dummy_plus(tokens)  # 最初にプラスをつける
    tokens = evaluate_times_divide(tokens)  # 掛け算割り算を先に計算
    tokens = evaluate_plus_minus(tokens) # プラスマイナス計算
    return tokens   

def main(line):
    tokens,brackets_count = tokenize(line)  # 数字と記号に分ける,括弧の数取得
    
    for i in range(brackets_count):
        brackets_left_index,brackets_right_index=find_smallest_bracket(tokens)#最小の括弧探す
        tokens=calculate_smallest_bracket(tokens,brackets_left_index,brackets_right_index)
     
    answer=calculate_tokens(tokens)
    return answer

def test(line):
    actual_answer=main(line)    
    expected_answer = eval(line)
    if abs(actual_answer - expected_answer) < 1e-8:
        print("PASS! (%s = %f)" % (line, expected_answer))
    else:
        print("FAIL! (%s should be %f but was %f)" %
              (line, expected_answer, actual_answer))


# Add more tests to this function :)
def run_test():
    print("==== Test started! ====")
    test("1")
    test("1+2")
    test("1.0+2.1-3")
    test("1.0+5*4")
    test("5*3*400000.9")
    test("2.1*3")
    test("1.0+2.0*3/6")
    test("4+5+6/6/6")
    test("5.6*7.845")
    test("5*(5-3)")
    test("(3.5+4*(2-1))/5")
    test("((3.5+4*(2.3-1))/4.2)*4")
    print("==== Test finished! ====\n")


run_test()

while True:
    print('> ', end="")
    line = input()  # 入力
    answer=main(line)   
    print("answer = %f\n" % answer)

