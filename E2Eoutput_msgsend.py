from cereal.messaging import PubMaster
from cereal import log, custom

# PubMasterの初期化（services.pyで定義されているサービス名を指定）
pm = PubMaster(['e2eOutput'])

# E2EOutputメッセージの生成
msg = log.Event.new_message()
msg.valid = True
msg.customReserved0 = custom.E2EOutput.new_message()
msg.customReserved0.vEgo = 12.34  # ここに車速[m/s]をセット
msg.customReserved0.steeringAngleDeg = 5.67  # ここに舵角[deg]をセット

# メッセージ送信
pm.send('e2eOutput', msg)