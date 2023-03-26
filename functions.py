from web3 import Web3
from config import *

def my_wallet_func(list):
    default_provider = get_default_provider()
    web3 = Web3(Web3.HTTPProvider(default_provider['provider']['rpc']))
    web3.eth.account.enable_unaudited_hdwallet_features()
    _wallets = []
    for seed in list:
        cWallet = web3.eth.account.from_key(seed)
        balance = web3.eth.get_balance(cWallet.address)
        nonce = web3.eth.get_transaction_count(cWallet.address)
        _wallets.append({'wallet': cWallet, 'balance': balance, 'nonce': nonce})

    return _wallets


def network_ask(): # выбор сетей для бриджа БЕЗ проверок (возвращает число в списке networks начиная с 1)
    chain_from = int(input('BRIDGE FROM?\n--------------------\nEthereum - 1\nArbitrum - 2\nOptimism - 3\nMatic - 4\nBSC - 5\nPlease type the number of the required network\n--------------------\n'))
    chain_to = int(input('BRIDGE TO?\n--------------------\nEthereum - 1\nArbitrum - 2\nOptimism - 3\nMatic - 4\nBSC - 5\nPlease type the number of the required network\n--------------------\n'))
    return chain_from, chain_to

    
def network_choose(currency, networks = networks): # выбор сетей для бриджа со всеми проверками
    try:
        while True:
            [chain_from, chain_to] = network_ask()
            if ((chain_from == chain_to) or (chain_from <= 0) or (chain_from > len(networks)) or (chain_to <= 0) or (chain_to > len(networks))):
                print('You need to type an integer from 1 to', len(networks),'or you tried to use the same bridges')  
                return network_choose()
            elif (token_fees[currency][networks[chain_to - 1]]['restricted'] or token_fees[currency][networks[chain_from - 1]]['restricted']):
                print('You cant send', currency, 'to (or from)', [networks[chain_to - 1]],'please try something different')
                return network_choose(currency)
            else:
                return networks[chain_from - 1], networks[chain_to - 1]
    except:
        print('Whoops, try again! Maybe you mistyped something?')
        return network_choose(currency)


def ask_transaction_count(): # спрашиваем у юзера количество транзакций
    try:
        trx_count = int(input('\nPlease, enter the quantity of transactions:\n'))
        return number_check(trx_count, ask_transaction_count)
    except:
        print('Whoops, try again')
        return ask_transaction_count()


def ask_amount(currency, chain_from, chain_to): #спрашиваем сколько токенов отправлять 
    try:
        min_price = transfer_limit[chain_from][chain_to][currency]['min']
        max_price = transfer_limit[chain_from][chain_to][currency]['max']
        print('What amount of', currency ,'do you want to bridge in one transaction?')
        amount = float(input())
        if (amount > min_price  and amount < max_price):
            return number_check(amount, ask_amount)
        else:
            print('The min amount is', min_price, 'and the max amount is', max_price,'please try again\n')
            return ask_amount(currency, chain_from, chain_to)
    except:
        print('Whoops, try again')
        return ask_amount(currency, chain_from, chain_to)

def ask_currency(coins = coins): #спрашиваем какую монетку кидать
    try:
        while True:
            currency = int(input('--------------------\nPlease choose the preferred coin to bridge and type the following number:\n\nETH - 1\nUSDC - 2\nUSDT - 3\nDAI - 4\n--------------------\n'))
            if (currency <= 0 or currency >= len(coins)):
                 print('You need to type an integer from 1 to', len(coins))  
                 return ask_currency()
            else:
                return coins[currency - 1]
    except:
        print('Whoops, try again! Maybe you mistyped something?')
        return ask_currency()


def number_check(num, func): #проверка на то больше ли число 0, в обратном случае выполняется заданная функция
    if num > 0:
        return num
    else:
        return func()