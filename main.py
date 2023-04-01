from web3 import Web3
from decimal import Decimal
from functions import *
from hexbytes import HexBytes
from multiprocessing.dummy import Pool

from time import sleep 
from random import randint


def bridge(user_info):
    wallet = user_info['wallet']
    chain_from = user_info['chain_from']
    provider_info = get_current_provider(chain_from)
    web3 = Web3(Web3.HTTPProvider(provider_info['rpc']))
    code = network_code[user_info['code']]
    currency = user_info['currency']
    amount = Decimal(user_info['amount'])

    nonce = web3.eth.get_transaction_count(wallet['wallet'].address)
    chain_id = network_chain_id[chain_from]


    gas = web3.eth.gas_price
    gas_limit = get_gas_limit(chain_from)
    total_transaction_gas_fees = web3.from_wei(Decimal(gas) * Decimal(gas_limit), 'ether')
    

    
    wallet_balance = web3.eth.get_balance(wallet['wallet'].address)
    wallet_address = wallet['wallet'].address



    user_info['balance'] = wallet_balance
    user_info['address'] = wallet_address
    user_info['total_transaction_gas_fees'] = total_transaction_gas_fees

    if chain_from == 'bsc' or chain_from == 'matic':
        unicorn = web3.eth.contract(address = token_contracts[chain_from][currency] , abi = ERC20_ABI )
        user_info['contract_decimals'] = Decimal(unicorn.functions.decimals().call())
        user_info['stable_balance'] = Decimal(unicorn.functions.balanceOf(wallet_address).call())


        if currency in ['usdc', 'usdt', 'dai']:
            user_info['is_stable'] = True


        value = int(Decimal(10 ** user_info['contract_decimals'] * amount)) // 10000 * 10000 + code
    elif ((user_info['currency']) != 'eth'): #инизиализация контракта если выбран альт-коин
        unicorn = web3.eth.contract(address = token_contracts[chain_from][currency] , abi = ERC20_ABI )
        user_info['contract_decimals'] = Decimal(unicorn.functions.decimals().call())
        user_info['stable_balance'] = Decimal(unicorn.functions.balanceOf(wallet_address).call())
        user_info['is_stable'] = True

        value = int(Decimal(10 ** user_info['contract_decimals'] * amount)) // 10000 * 10000 + code
    else:
        value = web3.to_wei(Decimal((amount) + total_transaction_gas_fees), 'ether')// 10000 * 10000 + code

    if bridge_check(user_info) == 0:
        return 0
    
    print ('Wallet address: ', wallet_address)


    match chain_from:
        case 'ethereum':
            match user_info['currency']:
                case 'eth':
                    tx = {'nonce': nonce, 
                          'to': HexBytes(eth_orbiter), 
                          'value': value,   
                          'gas': gas_limit, 
                          'gasPrice': gas }
                case 'usdt':
                     tx = unicorn.functions.transfer( usdt_orbiter , 
                        value,
                        ).build_transaction({
                         'chainId': chain_id,
                         'gas': gas_limit,
                         'maxFeePerGas': gas + web3.to_wei('1', 'gwei'),
                         'maxPriorityFeePerGas': web3.to_wei('1', 'gwei'),
                         'nonce': nonce,
                         })
                case 'usdc':
                     tx = unicorn.functions.transfer( usdc_orbiter , 
                        value,
                        ).build_transaction({
                         'chainId': chain_id,
                         'gas': gas_limit,
                         'maxFeePerGas': gas + web3.to_wei('1', 'gwei'),
                         'maxPriorityFeePerGas': web3.to_wei('1', 'gwei'),
                         'nonce': nonce,
                         })
                case 'dai':
                     tx = unicorn.functions.transfer( dai_orbiter , 
                        value,
                        ).build_transaction({
                         'chainId': chain_id,
                         'gas': gas_limit,
                         'maxFeePerGas': gas + web3.to_wei('1', 'gwei'),
                         'maxPriorityFeePerGas': web3.to_wei('1', 'gwei'),
                         'nonce': nonce,
                         })
        case 'arbitrum':
            match user_info['currency']:
                case 'eth': 
                    tx = {'nonce': nonce, 
                          'to': HexBytes(eth_orbiter), 
                          'value': value, 
                          'gas': gas_limit, 
                          'gasPrice': gas } 
                case 'usdt':
                     tx = unicorn.functions.transfer( usdt_orbiter, 
                        value,
                        ).build_transaction({
                         'chainId': chain_id,
                         'gas': gas_limit,
                         'maxFeePerGas': gas + web3.to_wei('1', 'gwei'),
                         'maxPriorityFeePerGas': web3.to_wei('1', 'gwei'),
                         'nonce': nonce,
                         })
                case 'usdc':
                     tx = unicorn.functions.transfer( usdc_orbiter , 
                        value,
                        ).build_transaction({
                         'chainId': chain_id,
                         'gas': gas_limit,
                         'maxFeePerGas': gas + web3.to_wei('1', 'gwei'),
                         'maxPriorityFeePerGas': web3.to_wei('1', 'gwei'),
                         'nonce': nonce,
                         })
                case 'dai':
                     tx = unicorn.functions.transfer( dai_orbiter , 
                        value,
                        ).build_transaction({
                         'chainId': chain_id,
                         'gas': gas_limit,
                         'maxFeePerGas': gas + web3.to_wei('1', 'gwei'),
                         'maxPriorityFeePerGas': web3.to_wei('1', 'gwei'),
                         'nonce': nonce,
                         })
        case 'optimism':
            match user_info['currency']:
                case 'eth':
                        tx = {'nonce': nonce, 
                          'to': eth_orbiter, 
                          'value': value, 
                          'gas': gas_limit, 
                          'gasPrice': gas }
                case 'usdt':
                     tx = unicorn.functions.transfer( usdt_orbiter , 
                        value,
                        ).build_transaction({
                         'chainId': chain_id,
                         'gas': gas_limit,
                         'maxFeePerGas': gas + web3.to_wei('1', 'gwei'),
                         'maxPriorityFeePerGas': web3.to_wei('1', 'gwei'),
                         'nonce': nonce,
                         })
                case 'usdc':
                     tx = unicorn.functions.transfer( usdc_orbiter , 
                        value,
                        ).build_transaction({
                         'chainId': chain_id,
                         'gas': gas_limit,
                         'maxFeePerGas': gas + web3.to_wei('1', 'gwei'),
                         'maxPriorityFeePerGas': web3.to_wei('1', 'gwei'),
                         'nonce': nonce,
                         })
                case 'dai':
                     tx = unicorn.functions.transfer( dai_orbiter , 
                        value,
                        ).build_transaction({
                         'chainId': chain_id,
                         'gas': gas_limit,
                         'maxFeePerGas': gas + web3.to_wei('1', 'gwei'),
                         'maxPriorityFeePerGas': web3.to_wei('1', 'gwei'),
                         'nonce': nonce,
                         })
        case 'matic':
            match user_info['currency']:
                case 'eth':
                    tx = unicorn.functions.transfer( weth_orbiter , 
                        value,
                        ).build_transaction({
                         'chainId': chain_id,
                         'gas': gas_limit,
                         'maxFeePerGas': gas + web3.to_wei('5', 'gwei'),
                         'maxPriorityFeePerGas': web3.to_wei('30', 'gwei'),
                         'nonce': nonce,
                         })
                case 'usdt':
                     tx = unicorn.functions.transfer( usdt_orbiter , 
                        value,
                        ).build_transaction({
                         'chainId': chain_id,
                         'gas': gas_limit,
                         'maxFeePerGas': gas + web3.to_wei('5', 'gwei'),
                         'maxPriorityFeePerGas': web3.to_wei('30', 'gwei'),
                         'nonce': nonce,
                         })
                case 'usdc':
                     tx = unicorn.functions.transfer( usdc_orbiter , 
                        value,
                        ).build_transaction({
                         'chainId': chain_id,
                         'gas': gas_limit,
                         'maxFeePerGas': gas + web3.to_wei('5', 'gwei'),
                         'maxPriorityFeePerGas': web3.to_wei('30', 'gwei'),
                         'nonce': nonce,
                         })
                case 'dai':
                     tx = unicorn.functions.transfer( dai_orbiter , 
                        value,
                        ).build_transaction({
                         'chainId': chain_id,
                         'gas': gas_limit,
                         'maxFeePerGas': gas + web3.to_wei('5', 'gwei'),
                         'maxPriorityFeePerGas': web3.to_wei('30', 'gwei'),
                         'nonce': nonce,
                         })
        case 'bsc':
            match user_info['currency']:
                case 'eth':
                    tx = unicorn.functions.transfer( eth_orbiter , 
                        value,
                        ).build_transaction({
                         'chainId': chain_id,
                         'gas': gas_limit,
                         'maxFeePerGas': gas + web3.to_wei('1', 'gwei'),
                         'maxPriorityFeePerGas': web3.to_wei('1', 'gwei'),
                         'nonce': nonce,
                         })
        case 'nova':
            match user_info['currency']:
                case 'eth':
                    tx = {'nonce': nonce, 
                          'to': HexBytes(eth_orbiter), 
                          'value': value, 
                          'gas': gas_limit,     
                          'gasPrice': gas }
                case 'usdc':
                     tx = unicorn.functions.transfer( usdc_orbiter , 
                        value,
                        ).build_transaction({
                         'chainId': chain_id,
                         'gas': gas_limit,
                         'maxFeePerGas': gas + web3.to_wei('1', 'gwei'),
                         'maxPriorityFeePerGas': web3.to_wei('1', 'gwei'),
                         'nonce': nonce,
                         })


    for i in range(user_info['trx_count']):

        signed_tx = web3.eth.account.sign_transaction(tx, wallet['wallet'].key)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

        print('TRANSACTION HASH:', web3.to_hex(tx_hash))

        tx['nonce'] += 1
        if hasattr(tx, 'gasPrice'):
            tx['gasPrice'] = web3.eth.gas_price
        
        sleep(randint(2,3)) # задержка между транзакциями чтобы не побрили


if (__name__ == "__main__"):
    with open('wallets.txt', 'r') as f:
        private_keys = f.read().splitlines()
    wallets = my_wallet_func(private_keys)
    currency = ask_currency()
    chain_from, chain_to = network_choose(currency)
    trx_count = ask_transaction_count()
    amount = ask_amount(currency, chain_from, chain_to) 
    trx_cost = (amount + 0.003 * amount + token_fees[currency][chain_to]['withholding_fee']) 
    total_trxs_cost = trx_cost * trx_count


    print(token_fees[currency][chain_to]['withholding_fee'])
    print('CHAIN FROM -> ', chain_from, '\nDESTINATION -> ', chain_to)
    print ('Quantity of transactions:', trx_count)
    print ('The currency is set to:', currency)
    print ('One transaction cost:',  trx_cost, '\nTotal:', trx_cost * trx_count)
    print ('TOTAL:', total_trxs_cost)
    print ('TRANSACTION COST IS ESTIMATED AND IT MAY BE BIGGER OR LOWER')

    
    threads = 1
    pool = Pool(threads)
    collections_user_info = []
    
    for wallet in wallets:
        user_info = {
            'amount': trx_cost,
            'currency': currency,
            'trx_count': trx_count,
            'chain_from': chain_from,
            'code': chain_to,
            'chain_to': chain_to,
            'wallet': wallet,
            'total_trxs_cost' : total_trxs_cost,
            'is_stable': False,
        }
        collections_user_info.append(user_info)

    pool.map(bridge, collections_user_info)