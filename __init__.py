from gym.envs.registration import register


register(
    id='GoEnv',
    entry_point='gym_go.envs:GoEnv'
)

"""
register(
    id='TradingEnv-v1',
    entry_point='gym_trading.envs:TradingEnv',
    kwargs = { 'use_settings': False }
)
"""