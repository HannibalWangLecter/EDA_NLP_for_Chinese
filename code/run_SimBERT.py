from nlpcda import Simbert
config = {
        'model_path': '/xxxx/chinese_simbert_L-12_H-768_A-12',
        'device': 'cuda',
        'max_len': 32,
        'seed': 1
}
simbert = Simbert(config=config)
sent = '把我的一个亿存银行安全吗'
synonyms = simbert.replace(sent=sent, create_num=5)
print(synonyms)


'''
[('我的一个亿，存银行，安全吗', 0.9871675372123718), 
('把一个亿存到银行里安全吗', 0.9352194666862488), 
('一个亿存银行安全吗', 0.9330801367759705), 
('一个亿的存款存银行安全吗', 0.92387855052948),
 ('我的一千万存到银行安不安全', 0.9014463424682617)]
'''