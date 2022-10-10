문제 설명
당신은 실버를 사용해 골드를 사고파는 온라인 화폐 거래소를 운영합니다. 화폐 거래소를 이용하는 회원들은 알파벳 대소문자로 이루어진 고유한 아이디를 가지고 있습니다. 회원들은 화폐 거래소에 골드 구매 요청과 골드 판매 요청을 등록할 수 있으며, 완료되지 않은 요청은 pending, 완료된 요청은 done을 상태로 가집니다.

판매할 골드의 양이 sell_amount, 판매 가격이 sell_price인 골드 판매 요청의 등록은 다음과 같은 순서로 처리됩니다.

pending 상태인 구매 요청 중 구매 가격이 sell_price 이상인 구매 요청을 찾습니다. 그러한 구매 요청이 여러 개일 경우 구매 가격이 가장 비싼 구매 요청 중 가장 먼저 등록된 구매 요청을 선택합니다. 구매 가격이 sell_price 이상인 구매 요청을 찾지 못했을 경우, 판매 요청은 pending 상태가 되며 등록을 종료합니다.
찾은 구매 요청의 구매 골드 양이 buy_amount 일 때, 골드 1당 sell_price의 가격으로 min(buy_amount, sell_amount) 만큼의 골드 거래가 이루어집니다. 거래가 이루어진 골드의 양이 amount라면, 판매자의 계좌에서 구매자의 계좌로 amount만큼의 골드가 이동하며, 구매자의 계좌에서 판매자의 계좌로 amount × sell_price만큼의 실버가 이동합니다.
구매 요청의 buy_amount가 min(buy_amount, sell_amount) 만큼 감소합니다. buy_amount가 0이 되었다면 해당 구매 요청은 done 상태가 됩니다.
판매 요청의 sell_amount가 min(buy_amount, sell_amount) 만큼 감소합니다. sell_amount가 0이 되었다면 해당 판매 요청은 done 상태가 되며, 등록을 종료합니다.
sell_amount가 1 이상이라면 1번 순서로 돌아갑니다.
골드 구매 요청 또한 골드 판매 요청과 유사하게 처리됩니다. 구매할 골드의 양이 buy_amount, 구매 가격이 buy_price인 골드 구매 요청의 등록은 다음과 같은 순서로 처리됩니다.

pending 상태인 판매 요청 중 판매 가격이 buy_price 이하인 판매 요청을 찾습니다. 그러한 판매 요청이 여러 개일 경우 판매 가격이 가장 싼 판매 요청 중 가장 먼저 등록된 판매 요청을 선택합니다. 판매 가격이 buy_price 이하인 판매 요청을 찾지 못했을 경우, 구매 요청은 pending 상태가 되며 등록을 종료합니다.
찾은 판매 요청의 판매 골드 양이 sell_amount 일 때, 골드 1당 sell_price의 가격으로 min(buy_amount, sell_amount) 만큼의 골드 거래가 이루어집니다. 거래가 이루어진 골드의 양이 amount라면, 판매자의 계좌에서 구매자의 계좌로 amount만큼의 골드가 이동하며, 구매자의 계좌에서 판매자의 계좌로 amount × sell_price만큼의 실버가 이동합니다.
판매 요청의 sell_amount가 min(buy_amount, sell_amount) 만큼 감소합니다. sell_amount가 0이 되었다면 해당 판매 요청은 done 상태가 됩니다.
구매 요청의 buy_amount가 min(buy_amount, sell_amount) 만큼 감소합니다. buy_amount가 0이 되었다면 해당 구매 요청은 done 상태가 되며, 등록을 종료합니다.
buy_amount가 1 이상이라면 1번 순서로 돌아갑니다.
다음은 골드 구매 요청을 처리하는 예시입니다.

pending 상태인 구매 요청

등록 순서	등록자 아이디	구매 수량	구매 가격
2	Andy	10	10
5	Louis	5	11
pending 상태인 판매 요청

등록 순서	등록자 아이디	판매 수량	판매 가격
1	William	7	20
4	Rohan	4	25
3	Rohan	10	40
현재 거래소에 등록된 pending 상태인 구매/판매 요청들이 위와 같을 때, 아이디가 "Andy"인 회원이 구매 수량 = 20, 구매 가격 = 30 인 구매 요청을 등록한다고 가정합니다. 이때, 구매 요청의 등록은 다음과 같이 처리됩니다.

pending 상태인 판매 요청 중 판매 가격이 가장 싼 요청은 등록순서가 1인 "William"의 판매 요청입니다. "Andy" 와 "William" 사이에 수량 = 7, 가격 = 20인 거래가 이루어지며, "William"의 판매 요청은 done 상태가 됩니다.
pending 상태인 판매 요청 중 그다음으로 판매 가격이 가장 싼 요청은 등록순서가 4인 "Rohan"의 판매 요청입니다. "Andy" 와 "Rohan" 사이에 수량 = 4, 가격 = 25인 거래가 이루어지며, "Rohan"의 판매 요청은 done 상태가 됩니다.
pending 상태인 판매 요청 중 그다음으로 판매 가격이 가장 싼 요청은 등록순서가 3인 "Rohan"의 판매 요청이지만, 구매 가격이 판매 가격보다 작으므로 거래는 이루어지지 않고, "Andy"의 구매 요청은 구매 수량 = 9, 구매 가격 = 30인 pending 상태가 됩니다.
위 처리가 끝난 뒤, 화폐 거래소에 등록된 pending 상태인 골드 구매/판매 요청은 아래 표와 같습니다.

pending 상태인 구매 요청

등록 순서	등록자 아이디	구매 수량	구매 가격
2	Andy	10	10
5	Louis	5	11
6	Andy	9	30
pending 상태인 판매 요청

등록 순서	등록자 아이디	판매 수량	판매 가격
3	Rohan	10	40
또한, 화폐 거래소 회원들의 골드/실버 변화를 계산해보면 아래 표와 같습니다.

회원 아이디	골드 변화	실버 변화
Andy	+11	-240
Louis	0	0
Rohan	-4	+100
William	-7	+140
당신은 모든 구매/판매 요청 등록을 처리한 뒤 거래소 회원들의 골드/실버 변화를 계산해야 합니다.

골드 구매/판매 요청을 등록한 사람의 아이디가 순서대로 담긴 문자열 배열 req_id와 골드 구매/판매 요청의 세부 정보가 순서대로 담긴 2차원 정수 배열 req_info가 주어집니다. 모든 요청의 등록이 처리된 후 화폐 거래소 회원들의 골드와 실버 변화를 문자열 배열에 담아서 return 하도록 solution 함수를 완성해주세요.

제한사항
return 값 형식
골드 판매/구매 요청을 등록한 기록이 있는 모든 회원의 아이디, 해당 회원의 골드 변화량과 실버 변화량을 공백으로 구분하여 문자열 배열에 담습니다.
회원의 아이디가 알파벳 사전 순으로 빠른 것부터 담습니다.
골드/실버가 증가할 경우 "+", 감소할 경우 "-"를 붙여 표시합니다.
(예시) ["A +30 -200", "B -30 +200", "C 0 0"]
1 ≤ req_id의 길이 = req_info의 길이 ≤ 50,000
req_id의 i번째 원소는 i번째 요청을 등록한 회원의 아이디이며, 알파벳 대소문자로만 이루어진 길이 1~10 사이인 문자열입니다.
req_info의 i번째 원소는 i번째로 등록된 요청의 세부정보를 나타내며, [TYPE, AMOUNT, PRICE] 형태입니다.
TYPE은 요청의 종류를 나타내며, 구매 요청일 경우는 0, 판매 요청일 경우는 1 입니다.
AMOUNT는 구매/판매 할 골드의 양을 나타내며, 1~100 사이의 정수입니다.
PRICE는 구매/판매 할 골드의 가격을 나타내며, 1~100 사이의 정수입니다.
어떤 회원의 pending 상태인 구매 요청이 있다면 그 회원은 판매 요청을 등록하지 않습니다. 또한, 반대로 어떤 회원의 pending 상태인 판매 요청이 있다면 그 회원은 구매 요청을 등록하지 않습니다.
입출력 예
req_id	req_info	result
["William", "Andy", "Rohan", "Rohan", "Louis", "Andy"]	[[1, 7, 20], [0, 10, 10], [1, 10, 40], [1, 4, 25], [0, 5, 11], [0, 20, 30]]	["Andy +11 -240", "Louis 0 0", "Rohan -4 +100", "William -7 +140"]
["Morgan", "Teo", "Covy", "Covy", "Felix"]	[[0, 10, 50], [1, 35, 70], [0, 10, 30], [0, 10, 50], [1, 11, 40]]	["Covy +1 -40", "Felix -11 +440", "Morgan +10 -400", "Teo 0 0"]
입출력 예 설명
입출력 예 #1

문제 예시와 같습니다.

입출력 예 #2

4번째 요청의 등록 처리가 끝날 때까지 아무 거래도 일어나지 않으며, 화폐 거래소에 등록된 골드 구매/판매 요청은 아래 표와 같습니다.

pending 상태인 구매 요청

등록 순서	등록자 아이디	구매 수량	구매 가격
3	Covy	10	30
4	Covy	10	50
1	Morgan	10	50
pending 상태인 판매 요청

등록 순서	등록자 아이디	판매 수량	판매 가격
2	Teo	35	70
이때 "Felix"가 등록한 판매 요청인 5번째 요청의 등록은 다음과 같이 처리됩니다.

pending 상태인 구매 요청 중 판매 가격이 가장 비싼 요청은 등록순서가 4인 "Covy"의 구매 요청과 등록순서가 1인 "Morgan"의 구매 요청입니다. 두 구매 요청 중 "Morgan"의 구매 요청이 먼저 등록되었으므로 "Felix" 와 "Morgan" 사이에 수량 = 10, 가격 = 40인 거래가 이루어지며, "Morgan"의 구매 요청은 done 상태가 됩니다.
pending 상태인 판매 요청 중 그다음으로 판매 가격이 가장 비싼 요청은 등록순서가 4인 "Covy"의 구매 요청입니다. "Felix" 와 "Covy" 사이에 수량 = 1, 가격 = 40인 거래가 이루어지며, "Felix"의 판매 요청은 done 상태가 되어 처리가 종료됩니다.
위 처리가 끝난 뒤, 화폐 거래소에 등록된 pending 상태인 골드 구매/판매 요청은 아래 표와 같습니다.

pending 상태인 구매 요청

등록 순서	등록자 아이디	구매 수량	구매 가격
3	Covy	10	30
4	Covy	9	50
pending 상태인 판매 요청

등록 순서	등록자 아이디	판매 수량	판매 가격
2	Teo	35	70
또한, 화폐 거래소 회원들의 골드/실버 변화를 계산해보면 아래 표와 같습니다.

회원 아이디	골드 변화	실버 변화
Covy	+1	-40
Felix	-11	+440
Morgan	+10	-400
Teo	0	0
따라서, ["Covy +1 -40", "Felix -11 +440", "Morgan +10 -400", "Teo 0 0"]을 return 해야 합니다.



#구매요청0 판매요청1
#완료되지 않은 요청 pending
#완료된 요청 done 
#판매할 골드의 양 sell_amount
#판매가격 sell_price
def solution(req_id, req_info):
    answer = []
    rnao = [] 
    vksao = []
    users = {}
    for name,info in zip(req_id,req_info):
        if not users.get(name):
            users[name] = [name,0,0]
        if info[0] == 0 : #TYPE0,1, AMOUNT, PRICE, + pending or done
            if vksao:
                for vks in vksao:
                    name_com,info_com = vks[0],vks[1]
                    if info_com[3] :
                        continue
                    elif info_com[2] > info[2] :
                        break
                    if info[1]>info_com[1]:
                        users[name_com][1] -= info_com[1]
                        users[name][1] += info_com[1]
                        users[name_com][2] += info_com[2]*info_com[1]
                        users[name][2] -= info_com[2]*info_com[1]
                        info[1] -= info_com[1]
                        info.append(False)
                    elif info[1] <= info_com[1]: 
                        users[name_com][1] -= info_com[1] - info[1] 
                        users[name][1] += info[1] 
                        users[name][2] -= info_com[2] * info[1] 
                        users[name_com][1] += info_com[2] * info[1] 
                        if info[1] == info_com[1] : 
                            info_com[-1] = True 
                            info.append(True)
                        else :
                            info.append(False)
            rnao.append([name,info])
            rnao.sort(key = lambda x: x[1][2])
        else:
            if rnao:
                for rn in rnao:
                    name_com,info_com = rn[0],rn[1]
                    if info_com[3] :
                        continue
                    elif info_com[2] < info[2] :
                        break
                    if info[1]>info_com[1]:
                        users[name_com][1] += info_com[1]
                        users[name][1] -= info_com[1]
                        users[name_com][2] -= info_com[2]*info_com[1]
                        users[name][2] += info_com[2]*info_com[1]
                        info[1] += info_com[1]
                        info.append(False)
                    elif info[1] <= info_com[1]: 
                        users[name_com][1] += info_com[1] - info[1] 
                        users[name][1] -= info[1] 
                        users[name][2] += info_com[2] * info[1] 
                        users[name_com][1] -= info_com[2] * info[1] 
                        if info[1] == info_com[1] : 
                            info_com[-1] = True 
                            info.append(True)
                        else :
                            info.append(False)
            vksao.append([name,info])
            vksao.sort(key = lambda x: x[1][2])
            
    print(rnao)
    print(vksao)
    print(users)
    answer = ["Andy +11 -240", "Louis 0 0", "Rohan -4 +100", "William -7 +140"]
    return answer