import pyupbit

access = "4xnCzO2GgjdmsSlLK3bRxunrnxeYjRcmwEMlX2PP"          # 본인 값으로 변경
secret = "xzhY9cbVxXiBNiUpUNGYULqdh5BbyDMmtVY8WerT"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XTZ"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회