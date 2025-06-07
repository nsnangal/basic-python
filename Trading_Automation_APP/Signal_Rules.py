signal_rules = {
    'RSI': {
        'type': 'rsi_crossover',
        'default_params': {'lower': 30, 'upper': 70}
    },
    'MACD': {
        'type': 'macd_cross',
        'default_params': {
            'macd_name': 'macd',
            'signal_name': 'macdsignal',
            'fastperiod': 12,
            'slowperiod': 26,
            'signalperiod': 9
        }
    },
    'SMA': {
        'type': 'ma_cross',
        'default_params': {'fast_name': 'sma_fast', 'slow_name': 'sma_slow'}
    },
    'EMA': {
        'type': 'ma_cross',
        'default_params': {'fast_name': 'ema_fast', 'slow_name': 'ema_slow'}
    },
    'WMA': {
        'type': 'ma_cross',
        'default_params': {'fast_name': 'wma_fast', 'slow_name': 'wma_slow'}
    },
    'STOCH': {
        'type': 'stoch_cross',
        'default_params': {'k_name': 'slowk', 'd_name': 'slowd', 'overbought': 80, 'oversold': 20}
    },
    'CCI': {
        'type': 'cci_crossover',
        'default_params': {'lower': -100, 'upper': 100}
    },
    'ADX': {
        'type': 'adx_trend',
        'default_params': {'threshold': 25, 'pdi_name': 'plus_di', 'mdi_name': 'minus_di'}
    },
    'BBANDS': {
        'type': 'bollinger_band',
        'default_params': {'price_name': 'real', 'upper_name': 'upperband', 'lower_name': 'lowerband'}
    },
    'ATR': {
        'type': 'atr_volatility',
        'default_params': {'threshold': 2}
    },
    'OBV': {
        'type': 'obv_trend',
        'default_params': {'sma_period': 20}
    },
    'MFI': {
        'type': 'mfi_crossover',
        'default_params': {'lower': 20, 'upper': 80}
    },
    'ROC': {
        'type': 'roc_crossover',
        'default_params': {'threshold': 0}
    },
    'ULTOSC': {
        'type': 'ultosc_crossover',
        'default_params': {'lower': 30, 'upper': 70}
    },
    'WILLR': {
        'type': 'williams_r_crossover',
        'default_params': {'lower': -80, 'upper': -20}
    },
    'TRIX': {
        'type': 'trix_crossover',
        'default_params': {'threshold': 0}
    },
    'SUPERTREND': {
        'type': 'supertrend_signal',
        'default_params': {
            'trend_name': 'supertrend',
            'atr_period': 10,
            'multiplier': 3
        }
    }
}
