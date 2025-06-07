import pandas as pd
import logging
from logging_manager import LoggerManager
from Signal_Rules import signal_rules


class SignalGenerator:

    @LoggerManager.log_function_call(logging.INFO)
    def __init__(self, indicator_results: dict, user_defined_rules: dict = None):
        """
        indicator_results : from UniversalIndicatorRunner.get_all_results()
        user_defined_rules : Optional custom rules for specific indicators (overrides defaults)
        """
        self.indicator_results = indicator_results
        self.user_defined_rules = user_defined_rules or {}
        self.signals = {}
        self.logger = LoggerManager().get_logger()

    @LoggerManager.log_function_call(logging.INFO)
    def auto_generate_logic(self):
        """
        Merge user-defined and default logic. User-defined gets priority.
        """
        logic_map = {}

        for key in self.indicator_results.keys():
            indicator_name = key.split('_')[0].upper()
        
            if indicator_name in self.user_defined_rules:
                logic_map[key] = self.user_defined_rules[indicator_name]
            elif indicator_name in signal_rules:
                logic_map[key] = {
                    'type': signal_rules[indicator_name]['type'],
                    'params': signal_rules[indicator_name].get('default_params', {})
                }
            else:
                self.logger.warning(f"No rule defined for indicator: {indicator_name}")

        return logic_map

    @LoggerManager.log_function_call(logging.INFO)
    def generate_signals(self):
        logic_map = self.auto_generate_logic()
        
        for key, logic in logic_map.items():
            try:
                
                indicator = self.indicator_results.get(key,{}).get('result',None)
                
                if indicator is None:
                    self.logger.warning(f"No indicator result for key: {key}")
                    continue

                logic_type = logic['type']
                logic_params = logic.get('params', {})

                index = None
                for attr in dir(indicator):
                    val = getattr(indicator, attr, None)
                    if isinstance(val, pd.Series):
                        index = val.index
                        break

                if index is None:
                    self.logger.warning(f"Could not determine index for key: {key}")
                    continue
                signal = pd.Series(0, index=index)

                if logic_type == 'rsi_crossover':
                    if logic_type == 'rsi_crossover':
                     rsi = getattr(indicator, 'real', None)
                     self.logger.info(rsi)     
                    if rsi is None:
                        rsi = getattr(indicator, 'rsi', None)
                        self.logger.info(rsi)
                    if rsi is not None:
                        lower, upper = logic_params.get('lower', 30), logic_params.get('upper', 70)
                        signal[(rsi > lower) & (rsi.shift(1) <= lower)] = 1
                        signal[(rsi < upper) & (rsi.shift(1) >= upper)] = -1
                elif logic_type == 'macd_cross':
                    macd = getattr(indicator, 'macd', None)
                    signal_line = getattr(indicator, 'macdsignal', None)
                    if macd is not None and signal_line is not None:
                        signal[(macd > signal_line) & (macd.shift(1) <= signal_line.shift(1))] = 1
                        signal[(macd < signal_line) & (macd.shift(1) >= signal_line.shift(1))] = -1
                elif logic_type == 'ma_cross':
                    fast = getattr(indicator, logic_params.get('fast_name'), None)
                    slow = getattr(indicator, logic_params.get('slow_name'), None)
                    if fast is not None and slow is not None:
                        signal[(fast > slow) & (fast.shift(1) <= slow.shift(1))] = 1
                        signal[(fast < slow) & (fast.shift(1) >= slow.shift(1))] = -1

                elif logic_type == 'stoch_cross':
                    k = getattr(indicator, logic_params.get('k_name'), None)
                    d = getattr(indicator, logic_params.get('d_name'), None)
                    overbought = logic_params.get('overbought', 80)
                    oversold = logic_params.get('oversold', 20)
                    if k is not None and d is not None:
                        signal[(k < oversold) & (k > d)] = 1
                        signal[(k > overbought) & (k < d)] = -1

                elif logic_type == 'cci_crossover':
                    cci = getattr(indicator, 'cci', None)
                    if cci is not None:
                        lower, upper = logic_params.get('lower', -100), logic_params.get('upper', 100)
                        signal[(cci > lower) & (cci.shift(1) <= lower)] = 1
                        signal[(cci < upper) & (cci.shift(1) >= upper)] = -1

                elif logic_type == 'adx_trend':
                    pdi = getattr(indicator, logic_params.get('pdi_name'), None)
                    mdi = getattr(indicator, logic_params.get('mdi_name'), None)
                    threshold = logic_params.get('threshold', 25)
                    if pdi is not None and mdi is not None:
                        signal[pdi > (mdi + threshold)] = 1
                        signal[mdi > (pdi + threshold)] = -1

                elif logic_type == 'bollinger_band':
                    price = getattr(indicator, logic_params.get('price_name'), None)
                    upper = getattr(indicator, logic_params.get('upper_name'), None)
                    lower = getattr(indicator, logic_params.get('lower_name'), None)
                    if price is not None and upper is not None and lower is not None:
                        signal[price < lower] = 1
                        signal[price > upper] = -1

                elif logic_type == 'atr_volatility':
                    atr = getattr(indicator, 'atr', None)
                    threshold = logic_params.get('threshold', 2)
                    if atr is not None:
                        signal[atr > threshold] = 1

                elif logic_type == 'obv_trend':
                    obv = getattr(indicator, 'obv', None)
                    obv_sma = obv.rolling(logic_params.get('sma_period', 20)).mean() if obv is not None else None
                    if obv is not None and obv_sma is not None:
                        signal[obv > obv_sma] = 1
                        signal[obv < obv_sma] = -1

                elif logic_type == 'mfi_crossover':
                    mfi = getattr(indicator, 'mfi', None)
                    lower, upper = logic_params.get('lower', 20), logic_params.get('upper', 80)
                    if mfi is not None:
                        signal[(mfi > lower) & (mfi.shift(1) <= lower)] = 1
                        signal[(mfi < upper) & (mfi.shift(1) >= upper)] = -1

                elif logic_type == 'roc_crossover':
                    roc = getattr(indicator, 'roc', None)
                    threshold = logic_params.get('threshold', 0)
                    if roc is not None:
                        signal[(roc > threshold) & (roc.shift(1) <= threshold)] = 1
                        signal[(roc < threshold) & (roc.shift(1) >= threshold)] = -1

                elif logic_type == 'ultosc_crossover':
                    ultosc = getattr(indicator, 'ultosc', None)
                    lower, upper = logic_params.get('lower', 30), logic_params.get('upper', 70)
                    if ultosc is not None:
                        signal[(ultosc > lower) & (ultosc.shift(1) <= lower)] = 1
                        signal[(ultosc < upper) & (ultosc.shift(1) >= upper)] = -1

                elif logic_type == 'williams_r_crossover':
                    willr = getattr(indicator, 'willr', None)
                    lower, upper = logic_params.get('lower', -80), logic_params.get('upper', -20)
                    if willr is not None:
                        signal[(willr > lower) & (willr.shift(1) <= lower)] = 1
                        signal[(willr < upper) & (willr.shift(1) >= upper)] = -1

                elif logic_type == 'trix_crossover':
                    trix = getattr(indicator, 'trix', None)
                    threshold = logic_params.get('threshold', 0)
                    if trix is not None:
                        signal[(trix > threshold) & (trix.shift(1) <= threshold)] = 1
                        signal[(trix < threshold) & (trix.shift(1) >= threshold)] = -1

                elif logic_type == 'supertrend_signal':
                    trend = getattr(indicator, logic_params.get('trend_name'), None)
                    if trend is not None:
                        signal[trend == True] = 1
                        signal[trend == False] = -1

                else:
                    self.logger.warning(f"Unsupported logic type: {logic_type}")

                self.signals[key] = signal

            except Exception as e:
                self.logger.error(f"Signal generation failed for {key}: {e}")

    @LoggerManager.log_function_call(logging.INFO)
    def get_signals(self, filter_by=None):
        if filter_by:
            return {k: v for k, v in self.signals.items() if k.startswith(filter_by.upper())}
        return self.signals
