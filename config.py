import json


def get_current_provider(name) -> {}:
    return providers[name]

def get_gas_limit(name) -> {}:
    return gas_limit[name]


ERC20_ABI = json.loads('''[{"inputs":[{"internalType":"string","name":"_name","type":"string"},{"internalType":"string","name":"_symbol","type":"string"},{"internalType":"uint256","name":"_initialSupply","type":"uint256"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint8","name":"decimals_","type":"uint8"}],"name":"setupDecimals","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]''')
EIP20_ABI = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]')  # noqa: 501


usdc_orbiter = '0x41d3D33156aE7c62c094AAe2995003aE63f587B3'
usdt_orbiter = '0xd7Aa9ba6cAAC7b0436c91396f22ca5a7F31664fC'
eth_orbiter = '0x80C67432656d59144cEFf962E8fAF8926599bCF8'
dai_orbiter = '0x095D2918B03b2e86D68551DCF11302121fb626c9'


networks = ['ethereum', 'arbitrum', 'optimism', 'matic', 'bsc', 'nova']
coins = ['eth','usdc','usdt','dai']


network_chain_id = {
    'ethereum' : 1,
    'arbitrum': 42161,
    'optimism': 10,
    'matic': 137,
    'bsc': 56,
    'nova': 42170,
}

gas_limit = {
    'ethereum': 21000,
    'arbitrum': 1000000 ,
    'optimism': 0,
    'matic': 0,
    'bsc': 0,
    'nova': 100000,
}

network_code = {
    'ethereum': 9001,
    'arbitrum': 9002,
    'optimism': 9007,
    'matic': 9006,
    'bsc': 9015,
    'nova': 9016,
}


providers = {
    'matic': {'chainId': 137,
              "rpc": 'https://rpc-mainnet.matic.quiknode.pro',
              "name": 'matic'},
    'bsc': {'chainId': 56,
            "rpc": 'https://rpc.ankr.com/bsc',
            # WARNING: ANKR BSC RPC is set for low gas fees, you may need to change it for higher transaction speed
            "name": 'bsc'},
    'ethereum': {'chainId': 1,
            "rpc": 'https://mainnet.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161',
            "name": 'ethereum'},
    'fuji': {'chainId': 43113,
             "rpc": 'https://api.avax-test.network/ext/bc/C/rpc',
             "name": 'fuji'},
    'mumbai': {'chainId': 80001,
               "rpc": 'https://matic-mumbai.chainstacklabs.com',
               "name": 'mumbai'},
    'rinkeby': {'chainId': 4,
                   "rpc": 'https://rinkeby.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161',
                   "name": 'rinkeby'},
    'optimism': {'chainId': 10,
            "rpc": 'https://mainnet.optimism.io',
            "name": 'optimism'},
    'arbitrum': {'chainId': 42161,
                "rpc": 'https://arb1.arbitrum.io/rpc',
                "name": 'arbitrum'},
    'nova': {'chainId': 42170,
                    "rpc": 'https://nova.arbitrum.io/rpc',
                    "name": 'nova'},
}

def get_default_provider(): # получаем провайдера эфириума для инициализации кошелька
    return {'provider': providers['ethereum']}

token_fees = {
    'usdc': {
        'matic': {
            'withholding_fee': 1.5,
            'restricted': False,
        },
        'optimism': {
            'withholding_fee': 1.8,
            'restricted': False
        },
        'arbitrum': {
            'withholding_fee': 1.8,
            'restricted': False
        },
        'bsc': {
            'withholding_fee': None,
            'restricted': True
        },
        'ethereum': {
            'withholding_fee': 12.8,
            'restricted': False
        },
        'nova' : {
            'withholding_fee': 1,
            'restricted': False
        }
    },
    'usdt': {
        'matic': {
            'withholding_fee': 2,
            'restricted': False
        },
        'optimism': {
            'withholding_fee': 2,
            'restricted': False
        },
        'arbitrum': {
            'withholding_fee': 2.5,
            'restricted': False
        },
        'bsc': {
            'withholding_fee': None,
            'restricted': True
        },
        'ethereum': {
            'withholding_fee': 12.8,
            'restricted': False
        },
        'nova' : {
            'withholding_fee': None,
            'restricted': True
        }
    },
    'dai': {
        'matic': {
            'withholding_fee': 1.5,
            'restricted': False
        },
        'optimism': {
            'withholding_fee': 2,
            'restricted': False
        },
        'arbitrum': {
            'withholding_fee': 2,
            'restricted': False
        },
        'bsc': {
            'withholding_fee': None,
            'restricted': True
        },
        'ethereum': {
            'withholding_fee': 12.8,
            'restricted': False
        },
        'nova' : {
            'withholding_fee': None,
            'restricted': True
        }
    },
    'eth': {
        'matic': {
            'withholding_fee': 0.0005,
            'restricted': False
        },
        'optimism': {
            'withholding_fee': 0.0005,
            'restricted': False
        },
        'arbitrum': {
            'withholding_fee': 0.0006,
            'restricted': False
        },
        'bsc': {
            'withholding_fee': 0.0005,
            'restricted': False
        },
        'ethereum': {
            'withholding_fee': 0.0062,
            'restricted': False
        },
        'nova' : {
            'withholding_fee': 0.0005,
            'restricted': False
        }
    },
}

token_contracts = {
    'ethereum': {
        'usdc' : '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48',
        'usdt': '0xdAC17F958D2ee523a2206206994597C13D831ec7',
        'dai': '0x6B175474E89094C44Da98b954EedeAC495271d0F'
    },
    'arbitrum': {
        'usdc': '0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8',
        'usdt': '0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9',
        'dai': '0xDA10009cBd5D07dd0CeCc66161FC93D7c9000da1'
    },
    'optimism': {
        'usdc': '0x7F5c764cBc14f9669B88837ca1490cCa17c31607',
        'usdt': '0x94b008aA00579c1307B0EF2c499aD98a8ce58e58',
        'dai': '0xDA10009cBd5D07dd0CeCc66161FC93D7c9000da1'
    },
    'matic': {
        'eth': '0x7ceB23fD6bC0adD59E62ac25578270cFf1b9f619',
        'usdc': '0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174',
        'usdt': '0xc2132D05D31c914a87C6611C10748AEb04B58e8F',
        'dai': '0x8f3Cf7ad23Cd3CaDbD9735AFf958023239c6A063'
    },
    'bsc': {
            'eth': '0x2170Ed0880ac9A755fd29B2688956BD959F933F8',
        },
    'nova': {
            'usdc': '0x750ba8b76187092B0D1E87E28daaf484d1b5273b'
        },
}

transfer_limit = {
    'ethereum': {
        'arbitrum': {
            'eth': {
                'min': 0.005,
                'max': 10
            },
            'usdc': {
                            'min': 0.005,
                            'max': 10000
                        },
            'usdt': {
                            'min': 0.005,
                            'max': 10000
                        },
            'dai': {
                            'min': 0.01,
                            'max': 3000
            },
        },
        'optimism': {
                    'eth': {
                        'min': 0.005,
                        'max': 10
                    },
                    'usdc': {
                                    'min': 0.005,
                                    'max': 10000
                                },
                    'usdt': {
                                    'min': 0.005,
                                    'max': 10000
                                },
                    'dai': {
                                    'min': 0.01,
                                    'max': 3000
                    },
        },
        'matic': {
                    'eth': {
                        'min': 0.005,
                        'max': 10
                    },
                    'usdc': {
                                    'min': 0.005,
                                    'max': 10000
                                },
                    'usdt': {
                                    'min': 0.005,
                                    'max': 10000
                                },
                    'dai': {
                                    'min': 0.01,
                                    'max': 3000
                    },
        },
        'bsc': {
                    'eth': {
                        'min': 0.005,
                        'max': 10
                    },
                },
        'nova': {
                    'eth': {
                        'min': 0.005,
                        'max': 5
                    },
                    'usdc': {
                                    'min': 0.005,
                                    'max': 10000
                    },
        },
    },
    'arbitrum': {
            'matic': {
                'eth': {
                    'min': 0.005,
                    'max': 10
                },
                'usdc': {
                                'min': 0.005,
                                'max': 10000
                            },
                'usdt': {
                                'min': 0.005,
                                'max': 10000
                            },
                'dai': {
                                'min': 0.01,
                                'max': 3000
                },
            },
            'optimism': {
                            'eth': {
                                'min': 0.005,
                                'max': 10
                            },
                            'usdc': {
                                            'min': 0.005,
                                            'max': 10000
                                        },
                            'usdt': {
                                            'min': 0.005,
                                            'max': 10000
                                        },
                            'dai': {
                                            'min': 0.01,
                                            'max': 3000
                            },
                        },
            'ethereum': {
                            'eth': {
                                'min': 0.005,
                                'max': 10
                            },
                            'usdc': {
                                            'min': 0.005,
                                            'max': 10000
                                        },
                            'usdt': {
                                            'min': 0.005,
                                            'max': 10000
                                        },
                            'dai': {
                                            'min': 0.01,
                                            'max': 3000
                            },
                        },
            'bsc': {
                            'eth': {
                                'min': 0.005,
                                'max': 10
                            },
                   },
            'nova': {
                    'eth': {
                        'min': 0.005,
                        'max': 5
                    },
                    'usdc': {
                                    'min': 0.005,
                                    'max': 10000
                    },
        },
    },
    'optimism': {
                'matic': {
                    'eth': {
                        'min': 0.005,
                        'max': 10
                    },
                    'usdc': {
                                    'min': 0.005,
                                    'max': 10000
                                },
                    'usdt': {
                                    'min': 0.005,
                                    'max': 10000
                                },
                    'dai': {
                                    'min': 0.01,
                                    'max': 3000
                    },
                },
                'nova': {
                    'eth': {
                        'min': 0.005,
                        'max': 5
                    },
                    'usdc': {
                                    'min': 0.005,
                                    'max': 10000
                    },
                },
                'arbitrum': {
                                'eth': {
                                    'min': 0.005,
                                    'max': 10
                                },
                                'usdc': {
                                                'min': 0.005,
                                                'max': 10000
                                            },
                                'usdt': {
                                                'min': 0.005,
                                                'max': 10000
                                            },
                                'dai': {
                                                'min': 0.01,
                                                'max': 3000
                                },
                            },
                'ethereum': {
                                'eth': {
                                    'min': 0.005,
                                    'max': 10
                                },
                                'usdc': {
                                                'min': 0.005,
                                                'max': 10000
                                            },
                                'usdt': {
                                                'min': 0.005,
                                                'max': 10000
                                            },
                                'dai': {
                                                'min': 0.01,
                                                'max': 3000
                                },
                            },
                'bsc': {
                                'eth': {
                                    'min': 0.005,
                                    'max': 10
                                },
                       },
        },
    'matic': {
                'optimism': {
                        'eth': {
                            'min': 0.005,
                            'max': 10
                        },
                        'usdc': {
                                        'min': 0.005,
                                        'max': 10000
                                    },
                        'usdt': {
                                        'min': 0.005,
                                        'max': 10000
                                    },
                        'dai': {
                                        'min': 0.01,
                                        'max': 3000
                        },
                    },
                'arbitrum': {
                                    'eth': {
                                        'min': 0.005,
                                        'max': 10
                                    },
                                    'usdc': {
                                                    'min': 0.005,
                                                    'max': 10000
                                                },
                                    'usdt': {
                                                    'min': 0.005,
                                                    'max': 10000
                                                },
                                    'dai': {
                                                    'min': 0.01,
                                                    'max': 3000
                                    },
                                },
                'ethereum': {
                                    'eth': {
                                        'min': 0.005,
                                        'max': 10
                                    },
                                    'usdc': {
                                                    'min': 0.005,
                                                    'max': 10000
                                                },
                                    'usdt': {
                                                    'min': 0.005,
                                                    'max': 10000
                                                },
                                    'dai': {
                                                    'min': 0.01,
                                                    'max': 3000
                                    },
                                },
                'bsc': {
                                    'eth': {
                                        'min': 0.005,
                                        'max': 10
                                    },
                           },
                'nova': {
                    'eth': {
                        'min': 0.005,
                        'max': 5
                    },
                    'usdc': {
                                    'min': 0.005,
                                    'max': 10000
                                },
        },
            },
    'bsc': {
                'optimism': {
                            'eth': {
                                'min': 0.005,
                                'max': 10
                            },
                        },
                'arbitrum': {
                                        'eth': {
                                            'min': 0.005,
                                            'max': 10
                                        }
                                    },
                'ethereum': {
                                        'eth': {
                                            'min': 0.005,
                                            'max': 10
                                        }
                                    },
                'matic': {
                                        'eth': {
                                            'min': 0.005,
                                            'max': 10
                                        },
                               },
                'nova': {
                    'eth': {
                        'min': 0.005,
                        'max': 5
                    },
                    'usdc': {
                                    'min': 0.005,
                                    'max': 10000
                                },
        },               
    },
    'nova': {
                'matic': {
                    'eth': {
                        'min': 0.005,
                        'max': 3
                    },
                    'usdc': {
                                    'min': 0.005,
                                    'max': 3000
                                },
                },
                'optimism': {
                    'eth': {
                        'min': 0.005,
                        'max': 3
                    },
                    'usdc': {
                                    'min': 0.005,
                                    'max': 3000
                                },
                },
                'arbitrum': {
                                'eth': {
                                    'min': 0.005,
                                    'max': 3
                                },
                                'usdc': {
                                                'min': 0.005,
                                                'max': 3000
                                            },
                            },
                'ethereum': {
                                'eth': {
                                    'min': 0.005,
                                    'max': 3
                                },
                                'usdc': {
                                                'min': 0.005,
                                                'max': 3000
                                            },
                            },
                'bsc': {
                                'eth': {
                                    'min': 0.005,
                                    'max': 3
                                },
                       },
        },
}